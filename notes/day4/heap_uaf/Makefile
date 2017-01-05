PROG=heap_uaf
CC=gcc
CFLAGS=-o $(PROG) -m32

$(PROG): $(PROG).c
	$(CC) $(CFLAGS) $^

clean:
	rm $(PROG)
