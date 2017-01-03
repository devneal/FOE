PROG = rop_exploit
CC = gcc
CFLAGS = -m32 -fno-stack-protector -mpreferred-stack-boundary=2

$(PROG): $(PROG).c
	$(CC) $(CFLAGS) -o $(PROG) $^

clean:
	rm $(PROG)
