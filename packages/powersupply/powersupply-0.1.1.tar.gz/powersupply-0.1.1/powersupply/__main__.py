import glob
import threading
import time

import gi
import logging
import os

from powersupply.platform import AXP803

try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, GObject, Gio, GdkPixbuf

gi.require_version('Handy', '0.0')
from gi.repository import Handy

logging.basicConfig(level=logging.DEBUG)


class PowerStatus:
    def __init__(self):
        self.battery_present = None
        self.battery_charging = None
        self.battery_capacity = None
        self.battery_voltage = None
        self.battery_current = None
        self.battery_health = None

        self.supply_type = None

        self.usb_present = None
        self.usb_current_limit = None

        self.ac_present = None


class DataPoller(threading.Thread):
    def __init__(self, callback):
        threading.Thread.__init__(self)
        self.callback = callback

    def run(self):
        supplies = self.get_supply_types()

        battery_present = os.path.join(supplies['bat'], 'present')
        battery_status = os.path.join(supplies['bat'], 'status')
        battery_health = os.path.join(supplies['bat'], 'health')
        battery_capacity = os.path.join(supplies['bat'], 'capacity')
        battery_voltage = os.path.join(supplies['bat'], 'voltage_now')

        supply_type = 'USB'

        if 'usb' in supplies:
            usb_present = os.path.join(supplies['usb'], 'present')
            usb_current_limit = os.path.join(supplies['usb'], 'input_current_limit')
        elif 'ac' in supplies:
            supply_type = 'AC'

        if 'ac' in supplies:
            ac_present = os.path.join(supplies['ac'], 'online')

        platform = None
        if os.path.isfile('/proc/device-tree/compatible'):
            compatible = self.read_sysfs_str('/proc/device-tree/compatible')
            if 'sun50i-a64' in compatible:
                # Probably Allwinner A64 with AXP803
                platform = AXP803()

        while True:
            ps = PowerStatus()
            ps.supply_type = supply_type
            ps.battery_present = self.read_sysfs(battery_present) == 1
            ps.usb_present = 'usb' in supplies and self.read_sysfs(usb_present) == 1
            ps.ac_present = 'ac' in supplies and self.read_sysfs(ac_present) == 1
            ps.battery_charging = self.read_sysfs_str(battery_status) == "Charging"
            try:
                ps.battery_health = self.read_sysfs_str(battery_health)
            except FileNotFoundError:
                ps.battery_health = 'Unknown'
            ps.battery_capacity = self.read_sysfs(battery_capacity)
            ps.battery_voltage = self.read_sysfs(battery_voltage) / 1000000.0
            ps.usb_current_limit = 'usb' in supplies and self.read_sysfs(usb_current_limit) / 1000000.0

            if platform:
                ps = platform.process(ps)

            GLib.idle_add(self.callback, ps)
            time.sleep(1)

    def read_sysfs(self, path):
        with open(path) as handle:
            return int(handle.read().strip())

    def read_sysfs_str(self, path):
        with open(path) as handle:
            return handle.read().strip()

    def get_supply_types(self):
        result = {}
        mapping = {
            'Battery': 'bat',
            'Mains': 'ac',
            'USB': 'usb'
        }
        for path in glob.glob('/sys/class/power_supply/*'):
            if not os.path.isfile(os.path.join(path, 'type')):
                print("Ignoring {} because it doesn't have a `type` file".format(path))
                continue
            with open(os.path.join(path, 'type')) as handle:
                type = handle.read().strip()

            if type in mapping:
                type = mapping[type]

            if type in result:
                result[type] = [result[type], path]
            else:
                result[type] = path
        return result


class PowersupplyApplication(Gtk.Application):
    def __init__(self, application_id, flags):
        Gtk.Application.__init__(self, application_id=application_id, flags=flags)
        self.connect("activate", self.new_window)

    def new_window(self, *args):
        AppWindow(self)


class AppWindow:
    def __init__(self, application):
        self.application = application
        builder = Gtk.Builder()
        with pkg_resources.path('powersupply', 'powersupply.glade') as ui_file:
            builder.add_from_file(str(ui_file))
        builder.connect_signals(Handler(builder))

        window = builder.get_object("main_window")
        window.set_application(self.application)
        window.show_all()

        Gtk.main()


class Handler:
    def __init__(self, builder):
        self.builder = builder
        self.window = builder.get_object('main_window')

        self.supply_type = builder.get_object('supply_type')
        self.bat_capacity = builder.get_object('bat_capacity')
        self.bat_voltage = builder.get_object('bat_voltage')
        self.bat_status = builder.get_object('bat_status')
        self.bat_health = builder.get_object('bat_health')
        self.bat_temp = builder.get_object('bat_temp')
        self.usb_charger = builder.get_object('usb_charger')
        self.usb_voltage = builder.get_object('usb_voltage')
        self.usb_current_limit = builder.get_object('usb_current_limit')

        thread = DataPoller(self.data_update)
        thread.daemon = True
        thread.start()

    def on_quit(self, *args):
        Gtk.main_quit()

    def data_update(self, result):
        if not isinstance(result, PowerStatus):
            return

        self.supply_type.set_text(result.supply_type)

        if result.battery_present:
            if result.battery_charging:
                bat_status = 'Charging'
            else:
                bat_status = 'Discharging'

            if result.battery_voltage is not None and result.battery_current is not None:
                power = result.battery_voltage * result.battery_current
                bat_status += ' ({:0.2f}W)'.format(power)

        else:
            bat_status = 'Not present'
        self.bat_status.set_text(bat_status)

        self.bat_capacity.set_text('{}%'.format(result.battery_capacity))
        self.bat_voltage.set_text('{:0.2f}V'.format(result.battery_voltage))
        self.bat_temp.set_text('')
        self.bat_health.set_text(result.battery_health)

        if result.usb_present:
            self.usb_current_limit.set_text('{:0.1f}A'.format(result.usb_current_limit))
            self.usb_voltage.set_text('')
            self.usb_charger.set_text('Connected')

        elif result.ac_present:
            self.usb_charger.set_text('Connected')
            self.usb_current_limit.set_text('')
            self.usb_voltage.set_text('')
        else:
            self.usb_current_limit.set_text('')
            self.usb_voltage.set_text('')
            self.usb_charger.set_text('Not connected')


def main():
    # To make sure libhandy is actually loaded in python
    Handy.Column()

    app = PowersupplyApplication("nl.brixit.powersupply", Gio.ApplicationFlags.FLAGS_NONE)
    app.run()


if __name__ == '__main__':
    main()
