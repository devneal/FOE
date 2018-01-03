CC = gcc
CFLAGS = -o $@ $@.c

clean:
	$(RM) memory_corruption ret_overwrite shellcode ret2libc use_leak make_leak canary_leak triangle 

example_elf:
	$(CC) $(CFLAGS)

triangle:
	$(CC) $(CFLAGS)

memory_corruption:
	$(CC) $(CFLAGS)

ret_overwrite:
	$(CC) $(CFLAGS) -fno-stack-protector

shellcode:
	$(CC) -o shellcode -fno-stack-protector -z execstack ret_overwrite.c

ret2libc:
	$(CC) $(CFLAGS) -fno-stack-protector -static

use_leak:
	$(CC) $(CFLAGS) -fno-stack-protector

make_leak:
	$(CC) $(CFLAGS) -fno-stack-protector

canary_leak:
	$(CC) $(CFLAGS)
