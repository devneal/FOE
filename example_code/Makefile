CC = gcc
CFLAGS = -o $@

clean:
	$(RM) core example_elf memory_corruption ret_overwrite shellcode ret2libc \
	      ret2libc_32 syscall use_leak make_leak canary_leak triangle

example_elf:
	$(CC) $(CFLAGS) $@.c

triangle:
	$(CC) $(CFLAGS) $@.c

memory_corruption:
	$(CC) $(CFLAGS) $@.c

ret_overwrite:
	$(CC) $(CFLAGS) $@.c -fno-stack-protector

shellcode:
	$(CC) $(CFLAGS)      -fno-stack-protector -z execstack ret_overwrite.c

ret2libc:
	$(CC) $(CFLAGS) $@.c -fno-stack-protector -static

ret2libc_32:
	$(CC) $(CFLAGS) $@.c -fno-stack-protector -static -m32

syscall:
	$(CC) $(CFLAGS) $@.c -fno-stack-protector -static

use_leak:
	$(CC) $(CFLAGS) $@.c -fno-stack-protector

make_leak:
	$(CC) $(CFLAGS) $@.c -fno-stack-protector

canary_leak:
	$(CC) $(CFLAGS) $@.c 
