CC = gcc
CFLAGS = -m32 -fno-stack-protector -z execstack -mpreferred-stack-boundary=2

shell_exploit: shell_exploit.c
	$(CC) $(CFLAGS) -o shell_exploit $^

clean:
	rm shell_exploit
