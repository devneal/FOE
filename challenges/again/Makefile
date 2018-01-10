PROG = again
CC = gcc
CFLAGS = -static -fno-stack-protector -g

$(PROG): $(PROG).c
	$(CC) $(CFLAGS) -o $(PROG) $^

clean:
	rm $(PROG)
