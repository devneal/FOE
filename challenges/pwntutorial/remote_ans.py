#!/usr/bin/python
from pwn import *

s = open("10000.txt").read().split(",")
primes = map(int, s)
r = remote("localhost", 8888)

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

print r.recvline()
