# -*- coding: utf-8 -*-

import sys
import dbus

bus = dbus.SessionBus()
proxy = bus.get_object('org.freedesktop.Notifications', '/org/freedesktop/Notifications')
interface = dbus.Interface(proxy,dbus_interface='org.freedesktop.Notifications')
interface.Notify('test_runner', 0, 
        '', 
        'title', 
        'message',
        [], 
        {}, 
        -1)
