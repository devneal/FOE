PROG=got_overwrite
CC=gcc
CFLAGS=-o $(PROG) -m32 -mpreferred-stack-boundary=2

$(PROG): $(PROG).c
	$(CC) $(CFLAGS) $^

clean:
	rm $(PROG)
