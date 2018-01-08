CC = gcc
CFLAGS = -fstack-protector -z relro -z now -pie -fPIC -g

all: lastday

lastday:
	$(CC) lastday.c $(CFLAGS) -o lastday

clean:
	rm -f lastday

.PHONY: all
