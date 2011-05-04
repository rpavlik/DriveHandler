# Part of DriveHandler
# Author: Ryan Pavlik

# https://github.com/rpavlik/DriveHandler

#          Copyright Iowa State University 2011.
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          http://www.boost.org/LICENSE_1_0.txt)

import os
import shutil

class ConfigFileHandler(object):
  """Base class for handlers that are responsible for updating some config file."""

  configdir = "config"

  def __init__(self, drive, hostPaths):
    self.drive = drive
    self.hostPaths = hostPaths
    self.configPath = os.path.join(self.drive.mountpoint, self.configdir)
    self.devicePaths = [os.path.join(self.configPath, os.path.basename(hostPath)) for hostPath in self.hostPaths]

    try:
      os.makedirs(self.configPath)
    except os.error:
      print "Config dir %s already exists." % self.configPath
    else:
      print "Created %s" % self.configPath

  def preUpdate(self):
    """Run before copying the updated config file. Default implementation does nothing."""
    pass

  def postUpdate(self):
    """Run after copying the updated config file. Default implementation does nothing."""
    pass

  def run(self):
    didPreUpdate = False
    for (devicePath, hostPath) in zip(self.devicePaths, self.hostPaths):
      if os.path.exists(devicePath):
        if not didPreUpdate:
          self.preUpdate()
          didPreUpdate = True

        print "Copying %s to %s" % (devicePath, hostPath)
        shutil.copyfile(devicePath, hostPath)

      else:
        print "Copying %s to %s" % (hostPath, devicePath)
        shutil.copyfile(hostPath, devicePath)
    if didPreUpdate:
      self.postUpdate()
