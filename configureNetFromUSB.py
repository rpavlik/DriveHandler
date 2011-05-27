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

import logging
logging.basicConfig(filename='/var/log/drivehandler', format='%(asctime)s %(message)s', level=logging.INFO)


logging.info("Importing DriveHandler")
import DriveHandler

logging.info("Setting config dir")
DriveHandler.ConfigFileHandler.configdir = "nosalt-configfiles"

class NetworkConfigHandler(DriveHandler.ConfigFileHandler):
  def __init__(self, drive):
    super(NetworkConfigHandler, self).__init__(drive, ["/etc/network/interfaces"])

  def postUpdate(self):
    print "Restarting networking..."
    subprocess.call(["service", "network-manager", "restart"])

def done():
  print "\a"
  logging.info("Done with something!")

def problem(ex):
  print "\a"
  logging.error("Problem reported by devicelistener.", ex)

logging.info("Setting DBusGMainLoop as default")
# Must come before creating the listener
DBusGMainLoop(set_as_default=True)


logging.info("Creating DeviceListener")
listener = DriveHandler.DeviceListener(
  handlerTypes = [NetworkConfigHandler],
  postUnmountCallbacks = [done],
  exceptionCallbacks = [problem]
)


logging.info("Creating mainloop")
loop = gobject.MainLoop()

logging.info("Starting DriveHandler mainloop...")
loop.run()
logging.info("DriveHandler exiting...")
