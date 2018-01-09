CC = gcc
CFLAGS = -o $@

clean:
	$(RM) core memory_corruption ret_overwrite shellcode 

memory_corruption:
	$(CC) $(CFLAGS) $@.c

ret_overwrite:
	$(CC) $(CFLAGS) $@.c -fno-stack-protector

shellcode:
	$(CC) $(CFLAGS)      -fno-stack-protector -z execstack ret_overwrite.c
