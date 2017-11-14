#!/usr/bin/python
from pwn import *

r = remote("localhost", 8888)

r.readuntil("word\n")
hex_str = r.readline().strip()
r.sendline(p64(int(hex_str, 16)))

r.readuntil("hex\n")
data_str = r.readline().strip()
ans = hex(u64(data_str))[2:]
r.sendline(ans)

print r.readline()
