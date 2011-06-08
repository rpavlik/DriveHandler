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
    super(NetworkConfigHandler, self).__init__(drive, ["/etc/network/interfaces", "/etc/resolv.conf"])

  def postUpdate(self):
    logging.info("Got an update, stopping networking...")
    subprocess.call(["service", "networking", "stop"])

    logging.info("Starting networking again...")
    subprocess.call(["service", "networking", "start"])

class VRPNConfigHandler(DriveHandler.ConfigFileHandler):
  def __init__(self, drive):
    super(VRPNConfigHandler, self).__init__(drive, ["/opt/vrpn-wiimote/etc/vrpn.cfg"])

  def postUpdate(self):
    logging.info("Got an update, stopping VRPN...")
    subprocess.call(["service", "vrpn", "stop"])

    logging.info("Starting VRPN again...")
    subprocess.call(["service", "vrpn", "start"])

def done():
  print "\a"
  logging.info("Done with something!")
  subprocess.call(["beep"])

def problem(ex):
  print "\a"
  logging.error("Problem reported by devicelistener.", ex)
  subprocess.call(["beep", "-r", "3"])


logging.info("Setting DBusGMainLoop as default")
# Must come before creating the listener
DBusGMainLoop(set_as_default=True)


logging.info("Creating DeviceListener")
listener = DriveHandler.DeviceListener(
  handlerTypes = [NetworkConfigHandler, VRPNConfigHandler],
  postUnmountCallbacks = [done],
  exceptionCallbacks = [problem]
)


logging.info("Creating mainloop")
loop = gobject.MainLoop()

logging.info("Starting DriveHandler mainloop...")
loop.run()
logging.info("DriveHandler exiting...")
