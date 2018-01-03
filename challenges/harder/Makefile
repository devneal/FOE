PROG = harder
CC = gcc
CFLAGS = -static -fno-stack-protector

$(PROG): $(PROG).c
	$(CC) $(CFLAGS) -o $(PROG) $^

clean:
	rm $(PROG)
