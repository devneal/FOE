CC = gcc
CFLAGS = -o $@

clean:
	$(RM) core ret2libc ret2libc_32 syscall use_leak

ret2libc:
	$(CC) $(CFLAGS) $@.c -fno-stack-protector -static

ret2libc_32:
	$(CC) $(CFLAGS) $@.c -fno-stack-protector -static -m32

syscall:
	$(CC) $(CFLAGS) $@.c -fno-stack-protector -static

use_leak:
	$(CC) $(CFLAGS) $@.c -fno-stack-protector
