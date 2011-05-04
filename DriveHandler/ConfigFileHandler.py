import os
import shutil

class ConfigFileHandler(object):
  """Base class for handlers that are responsible for updating some config file."""

  configdir = "config"

  def __init__(self, drive, hostPath):
    self.drive = drive
    self.hostPath = hostPath
    self.configPath = os.path.join(self.drive.mountpoint, self.configdir)
    self.devicePath = os.path.join(self.configPath, os.path.basename(hostPath))

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
    if os.path.exists(self.devicePath):
      self.preUpdate()
      print "Copying %s to %s" % (self.devicePath, self.hostPath)
      shutil.copyfile(self.devicePath, self.hostPath)
      self.postUpdate()

    else:
      print "Copying %s to %s" % (self.hostPath, self.devicePath)
      shutil.copyfile(self.hostPath, self.devicePath)

