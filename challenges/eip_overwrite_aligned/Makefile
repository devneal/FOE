CC = gcc
CFLAGS = -m32 -fno-stack-protector -z execstack -mpreferred-stack-boundary=2

eip_overwrite: eip_overwrite.c
	$(CC) $(CFLAGS) -o eip_overwrite $^

clean:
	rm eip_overwrite
