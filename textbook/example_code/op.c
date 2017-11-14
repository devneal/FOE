#include <stdio.h>

int main(void) {
    unsigned int a = 3;
    unsigned int b = 2;
    unsigned int c = a * b;
    scanf("%d", &a);
    if (a - b < 0) {
        printf("wut.\n");
    }
    return 0;
}
