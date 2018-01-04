CC = gcc
CFLAGS = -fstack-protector -z relro -z now -pie -fPIC

all: lastday

lastday:
	$(CC) lastday.c $(CFLAGS) -o lastday

clean:
	rm -f lastday

.PHONY: all
