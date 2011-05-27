DriveHandler
============

<https://github.com/rpavlik/DriveHandler>

Introduction
------------

Python code to wait for USB devices to be inserted on Linux, mount them,
run some handlers, then unmount. Written for a headless appliance/server
to be able to reconfigure from a USB key, shared because there are a lot
of partial solutions out there.

Using
-----

To be able to run this on ubuntu-server 11.04 you'll need some extra
packages. Most of them are probably already installed, so this line is
longer than strictly necessary for most.

> sudo apt-get install python python-gobject python-dbus dbus udisks

The `configureNetFromUSB.py` file is an example app using this system.
It requires running as "sudo" because it restarts networking after:
otherwise you may not need root privs to run this script. This script
also requires the "beep" program to provide assistance indicating when
USB transfers or errors have occurred. A simpler example is in
`sillyexample.py`.

You can edit and copy `drivehandler.conf` to `/etc/init` on systems that
use Upstart (like recent Ubuntu) to make it launch on startup.

Uses python-dbus to access udisks (formerly DeviceKit-disks). Works on
Ubuntu 10.04 and Ubuntu Server 11.04, that's all I've tested.

If you're trying this on a desktop (which already has GNOME
auto-mounting), you can stop the auto-mounter first:

> killall -STOP gvfs-gdu-volume-monitor

then resume it when you're done:

> killall -CONT gvfs-gdu-volume-monitor

Author
------
Ryan Pavlik

 - <rpavlik@iastate.edu>

 - <abiryan@ryand.net>

 - <http://academic.cleardefinition.com/>

License
-------
> Copyright Iowa State University 2011.
>
> Distributed under the Boost Software License, Version 1.0.
>
> (See accompanying file `LICENSE_1_0.txt` or copy at
> <http://www.boost.org/LICENSE_1_0.txt>)

Thanks/Links
------------

- <http://www.freedesktop.org/wiki/Software/udisks>

- <http://stackoverflow.com/questions/5067005/python-udisks-enumerating-device-information>

- <http://moserei.de/2010/01/08/accessing-devicekit-with-dbus-and-python.html>

- <http://stackoverflow.com/questions/5109879/usb-devices-udev-and-d-bus>

- <http://cgit.freedesktop.org/udisks/tree/tests/run>
