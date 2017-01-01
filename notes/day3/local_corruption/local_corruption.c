#include <stdio.h>

int main(void) {
    unsigned int a = 0x00000000;

    char buf[120];
    printf("Hi! What's your name? ");
    gets(buf);

    if (a == 0x0BADF00D)
        printf("Congratulations %s!!!\n", buf);
    else
        printf("Sorry %s, but a = 0x%08x\n", buf, a);

    return 0;
}
