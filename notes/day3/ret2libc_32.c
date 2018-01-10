#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

void empty(void) {
    system("echo You don\\'t have permission to perform this action.");
}

void win(void) {
    system("echo Access granted.");
}

void lose(void) {
    system("echo Invalid auth token.");
}

typedef struct auth {
    long int token;
    char buf[64];
} auth;

void prompt_user() {  
    auth a;
    memset(a.buf, 0, 64);
    a.token = 0;

    system("echo Enter the password:");
    read(0, a.buf, 100);

    if (a.token == 0) {
        empty();
    } else if (a.token == 0xdeadbeef) {
        win();
    } else {
        lose();
    }
}

int main(void) {
    prompt_user();
}
