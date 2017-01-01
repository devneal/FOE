CC = gcc
CFLAGS = -m32 -fno-stack-protector -z execstack -mpreferred-stack-boundary=2

local_corruption: local_corruption.c
	$(CC) $(CFLAGS) -o local_corruption $^

clean:
	rm local_corruption
