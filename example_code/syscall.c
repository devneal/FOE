#include <stdio.h>
#include <string.h>
#include <unistd.h>

void empty(void) {
    printf("You don't have permission to perform this action.\n");
}

void win(void) {
    printf("Access granted.\n");
}

void lose(void) {
    printf("Invalid auth token.\n");
}

typedef struct auth {
    long int token;
    char buf[64];
} auth;

int main(void) {
    auth a;
    memset(a.buf, 0, 64);
    a.token = 0;

    puts("We removed the calls to system().");
    puts("Now you'll never call /bin/sh");
    printf("Enter the password:\n");
    read(0, a.buf, 400);

    if (a.token == 0) {
        empty();
    } else if (a.token == 0xdeadbeef) {
        win();
    } else {
        lose();
    }
}
