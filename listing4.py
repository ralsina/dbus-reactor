# -*- coding: utf-8 -*-

import sys
import dbus
import dbus.mainloop.qt
from PyQt4 import QtCore

app=QtCore.QCoreApplication(sys.argv)
mainloop=dbus.mainloop.qt.DBusQtMainLoop(set_as_default=True)
systemBus = dbus.SystemBus()
sessionBus = dbus.SessionBus()

notify_proxy = sessionBus.get_object('org.freedesktop.Notifications', '/org/freedesktop/Notifications')
notifier = dbus.Interface(notify_proxy,dbus_interface='org.freedesktop.Notifications')

hal_proxy = systemBus.get_object('org.freedesktop.Hal', '/org/freedesktop/Hal/Manager')
manager = dbus.Interface(hal_proxy,dbus_interface='org.freedesktop.Hal.Manager')
kbd_dev = manager.FindDeviceByCapability('input.keyboard')[0]

kbd=dbus.Interface( systemBus.get_object('org.freedesktop.Hal', kbd_dev),
    dbus_interface='org.freedesktop.Hal.Device')

dbus.set_default_main_loop(mainloop)

def handler(*args,**kwargs):
    print "got signal from %s" % kwargs
    title=kwargs['message'].get_args_list()[1].replace('-',' ').title()
    notifier.Notify('System',0,'',title,'',[],{},-1)
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
