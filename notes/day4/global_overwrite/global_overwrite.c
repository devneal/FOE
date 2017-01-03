#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

unsigned int cant_touch_this = 0;

int main(int argc, char **argv) {
    printf(argv[1]);
    printf("\n");

    if (cant_touch_this == 0)
        printf("I told you homeboy u can't touch this\n");
    else
        printf("Darn...\n");
}

