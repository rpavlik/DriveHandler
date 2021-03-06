# Part of DriveHandler
# Author: Ryan Pavlik

# https://github.com/rpavlik/DriveHandler

#          Copyright Iowa State University 2011.
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          http://www.boost.org/LICENSE_1_0.txt)

import dbus
from USBDrive import USBDrive

class DeviceListener(object):
  def __init__(self, handlerTypes = [], postUnmountCallbacks = [], exceptionCallbacks = []):
    self.bus = dbus.SystemBus()
    self.ud_manager_obj = self.bus.get_object("org.freedesktop.UDisks", "/org/freedesktop/UDisks")
    self.ud_manager = dbus.Interface(self.ud_manager_obj, 'org.freedesktop.UDisks')
    self.ud_manager.connect_to_signal("DeviceAdded", self.handleDevice)
    self.handlerTypes = handlerTypes
    self.postUnmountCallbacks = postUnmountCallbacks
    self.exceptionCallbacks = exceptionCallbacks

  def handleDevice(self, dev):
    drive = USBDrive(dev)
    drive.mount()
    try:
      for handlerType in self.handlerTypes:
        h = handlerType(drive)
        h.run()
    except Exception as ex:
      print "Caught an exception... %s" % ex
      for callback in self.exceptionCallbacks:
        callback(ex)
    finally:
      drive.unmount()
      drive.eject()
      for callback in self.postUnmountCallbacks:
        callback()

