# requires packages:
# python python-gobject python-dbus dbus udisks
import gobject
from dbus.mainloop.glib import DBusGMainLoop
import subprocess

import DriveHandler

class SimpleConfigHandler(DriveHandler.ConfigFileHandler):
  """Simple config file handler class that calls this file a config file."""
  def __init__(self, drive):
    super(SimpleConfigHandler, self).__init__(drive, [__file__])

def unmountCallback():
  print "Unmount callback!"

def exceptionCallback(ex):
  print "Exception callback!"

# Must come before creating the listener
DBusGMainLoop(set_as_default=True)

# Automatically registers for signals when created
listener = DriveHandler.DeviceListener(
  handlerTypes = [SimpleConfigHandler],
  postUnmountCallbacks = [unmountCallback],
  exceptionCallbacks = [exceptionCallback]
)

loop = gobject.MainLoop()

# Never returns
loop.run()
