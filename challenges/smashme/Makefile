PROG = smashme
CC = gcc
CFLAGS = -fno-stack-protector -z execstack

$(PROG): $(PROG).c
	$(CC) $(CFLAGS) -o $(PROG) $^

clean:
	rm $(PROG)
