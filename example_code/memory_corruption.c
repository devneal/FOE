#include <stdio.h>
#include <string.h>

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
    char buf[64];
    long int token;
} auth;

int main(void) {
    auth a;
    memset(a.buf, 0, 64);
    a.token = 0;

    printf("Enter the password:\n");
    scanf("%s", a.buf);

    if (a.token == 0) {
        empty();
    } else if (a.token == 0xdeadbeef) {
        win();
    } else {
        lose();
    }
}
