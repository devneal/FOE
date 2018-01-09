#!/usr/bin/python
from pwn import *

s = open("10000.txt").read().split(",")
primes = map(int, s)
r = remote("lox.xvm.mit.edu", 22000)

r.readuntil("numbers?\n")
ans1 = str(sum(primes))
r.sendline(ans1)

r.readuntil(")?\n")
mod = 1000000007
ans2 = str(reduce(lambda x, y: (x * y) % mod, primes))
r.sendline(ans2)

r.readuntil("What's the ")
pos = int(r.readuntil("th", drop=True))
r.readuntil("number?\n")
ans3 = str(primes[pos - 1])
r.sendline(ans3)

print r.readline()

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

r.readuntil("word\n")
hex_str = r.readline().strip()
r.sendline(p64(int(hex_str, 16)))

r.readuntil("hex\n")
data_str = r.readline().strip()
ans = hex(u64(data_str))[2:]
r.sendline(ans)

print r.readline()
print r.readline()
