CC = gcc
CFLAGS = -o $@

clean:
	$(RM) core make_leak canary_leak

make_leak:
	$(CC) $(CFLAGS) $@.c -fno-stack-protector

canary_leak:
	$(CC) $(CFLAGS) $@.c 
