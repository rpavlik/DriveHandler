#!/usr/bin/env python
# Part of DriveHandler
# Author: Ryan Pavlik

# https://github.com/rpavlik/DriveHandler

#          Copyright Iowa State University 2011.
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          http://www.boost.org/LICENSE_1_0.txt)

import gobject
from dbus.mainloop.glib import DBusGMainLoop
import subprocess

import DriveHandler

class NetworkConfigHandler(DriveHandler.ConfigFileHandler):
  def __init__(self, drive):
    super(NetworkConfigHandler, self).__init__(drive, ["/etc/network/interfaces"])

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
