# -*- coding: utf-8 -*-

import sys
import dbus
import dbus.mainloop.qt
from PyQt4 import QtCore

app=QtCore.QCoreApplication(sys.argv)
mainloop=dbus.mainloop.qt.DBusQtMainLoop(set_as_default=True)
bus = dbus.SystemBus()

hal_proxy = bus.get_object('org.freedesktop.Hal', '/org/freedesktop/Hal/Manager')
manager = dbus.Interface(hal_proxy,dbus_interface='org.freedesktop.Hal.Manager')
kbd_dev = manager.FindDeviceByCapability('input.keyboard')[0]

kbd=dbus.Interface( bus.get_object('org.freedesktop.Hal', kbd_dev),
    dbus_interface='org.freedesktop.Hal.Device')

dbus.set_default_main_loop(mainloop)

def handler(*args,**kwargs):
    print "got signal from %s" % kwargs
    print kwargs['message'].get_args_list()

def setHook():
    kbd.connect_to_signal('Condition',handler,sender_keyword='sender', 
        destination_keyword='dest', 
        interface_keyword='interface', 
        member_keyword='member',
        path_keyword='path',
        message_keyword='message')

setHook()
print 'Entering loop'
app.exec_()
