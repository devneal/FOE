PROG = warmup
CC = gcc
CFLAGS = -Wall -fno-stack-protector

$(PROG): $(PROG).c
	$(CC) $(CFLAGS) -o $(PROG) $^

clean:
	rm $(PROG)
