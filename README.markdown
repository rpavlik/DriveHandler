DriveHandler
------------

<https://github.com/rpavlik/DriveHandler>

Python code to wait for USB devices to be inserted on Linux, mount them,
run some handlers, then unmount. Written for a headless appliance/server
to be able to reconfigure from a USB key, shared because there are a lot
of partial solutions out there.

To be able to run this on ubuntu-server 11.04 you'll need some extra
packages. Most of them are probably already installed, so this line is
longer than strictly necessary for most.

> sudo apt-get install python python-gobject python-dbus dbus udisks

The `configureNetFromUSB.py` file is an example app using this system.
It requires running as "sudo" because it restarts network-manager after:
otherwise you may not need root privs to run this script. A simpler
example is in `sillyexample.py`.

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
