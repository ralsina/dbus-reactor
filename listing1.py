# -*- coding: utf-8 -*-

import sys
import dbus

bus = dbus.SystemBus()
proxy = bus.get_object('org.freedesktop.Hal', '/org/freedesktop/Hal/Manager')
interface = dbus.Interface(proxy,dbus_interface='org.freedesktop.Hal.Manager')
print interface.FindDeviceByCapability('input.keyboard')[0]
