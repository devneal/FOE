#!/usr/bin/python
from pwn import *

r = remote("localhost", 8888)

r.readuntil("data\n")
hex_str = r.readline().strip()
r.sendline(unhex(hex_str))

r.readuntil("hex\n")
hex_str = r.readline().strip()
r.sendline(enhex(hex_str))

r.readuntil("data\n")
hex1 = r.readline().strip()
hex2 = r.readline().strip()
r.sendline(xor(unhex(hex1), unhex(hex2)))

print r.readline()
