# requires packages:
# python python-gobject python-dbus dbus udisks
import gobject
from dbus.mainloop.glib import DBusGMainLoop
import subprocess

import DriveHandler

class NetworkConfigHandler(DriveHandler.ConfigFileHandler):
  def __init__(self, drive):
    super(NetworkConfigHandler, self).__init__(drive, "/etc/network/interfaces")

  def postUpdate(self):
    print "Restarting networking..."
    subprocess.call(["service", "network-manager", "restart"])

def done():
  print "\a"

def problem(ex):
  print "\a"

# Must come before creating the listener
DBusGMainLoop(set_as_default=True)

listener = DriveHandler.DeviceListener(
  handlerTypes = [NetworkConfigHandler],
  postUnmountCallbacks = [done],
  exceptionCallbacks = [problem]
)

loop = gobject.MainLoop()
loop.run()
