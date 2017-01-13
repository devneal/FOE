#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void scramble(char* s, unsigned char c) {
    for (int i=0; i<(int)strlen(s); i++)
        s[i] ^= c;
}

int main(void) {
    //char s[] = "flag{x0r_15n7_3ncryp710n}";

    unsigned char secret[] = {0x29, 0x23, 0x2e, 0x28, 0x34,
                              0x37, 0x7f, 0x3d, 0x10, 0x7e,
                              0x7a, 0x21, 0x78, 0x10, 0x7c,
                              0x21, 0x2c, 0x3d, 0x36, 0x3f,
                              0x78, 0x7e, 0x7f, 0x21, 0x32,
                              0x00};

    unsigned char key1 = 0x50;
    unsigned char key2 = 0x35;
    unsigned char key3 = 0x2a;

    unsigned char input[26];
    scanf("%25s", input);

    scramble((char *)input, key1);
    scramble((char *)input, key2);
    scramble((char *)input, key3);

    if (strcmp((char *)input, (char *)secret) == 0)
        printf("Congratulations!!!\n");
    else
        printf("Try again...\n");

    return 0;
}
