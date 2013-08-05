import dbus
import pyperclip

session_bus = dbus.SessionBus()

player = session_bus.get_object('org.mpris.clementine','/Player')
iface = dbus.Interface(player, dbus_interface='org.freedesktop.MediaPlayer')

metadata = iface.GetMetadata()

#string declaration
artist = metadata["artist"]
title = metadata["title"]
#album = metadata["album"]

pyperclip.copy("#np: " + artist + " - " + title)
spam = pyperclip.paste()

