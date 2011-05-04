import dbus

class DeviceListener(object):
  def __init__(self, handlerTypes = []):
    self.bus = dbus.SystemBus()
    self.ud_manager_obj = self.bus.get_object("org.freedesktop.UDisks", "/org/freedesktop/UDisks")
    self.ud_manager = dbus.Interface(self.ud_manager_obj, 'org.freedesktop.UDisks')
    self.ud_manager.connect_to_signal("DeviceAdded", self.handleDevice)
    self.handlerTypes = handlerTypes

  def __beep(self):
    print "\a"

  def handleDevice(self, dev):
    drive = USBDrive(dev)
    drive.mount()
    try:
      for handlerType in self.handlerTypes:
        h = handlerType(drive)
        h.run()
    except Exception as ex:
      print "Caught an exception... %s" % ex

      beep()
    finally:
      drive.unmount()
      drive.eject()
      beep()

