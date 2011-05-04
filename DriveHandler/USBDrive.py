import dbus
import subprocess

class USBDrive(object):
  def __init__(self, dev):
    self.dev = dev
    self.device_obj = dbus.SystemBus().get_object("org.freedesktop.UDisks", dev)
    self.dev_methods = dbus.Interface(self.device_obj, dbus_interface='org.freedesktop.UDisks.Device')
    #self.dev_props = dbus.Interface(self.device_obj, dbus.PROPERTIES_IFACE)

  def mount(self):
    print "Waiting for udisks to settle..."
    subprocess.call(['udevadm', 'settle'])
    print "Mounting %s" % self.dev
    self.mountpoint = self.dev_methods.FilesystemMount('', [])

  def unmount(self):
    print "Unmounting %s" % self.dev
    self.dev_methods.FilesystemUnmount(dbus.Array([], 's'))
    self.mountpoint = None

  def eject(self):
    print "Ejecting %s" % self.dev
    self.dev_methods.DriveEject(dbus.Array([], 's'))

