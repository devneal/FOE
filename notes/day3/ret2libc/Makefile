CC = gcc
CFLAGS = -m32 -fno-stack-protector -mpreferred-stack-boundary=2

ret2libc_exploit: ret2libc_exploit.c
	$(CC) $(CFLAGS) -o ret2libc_exploit $^

clean:
	rm ret2libc_exploit
