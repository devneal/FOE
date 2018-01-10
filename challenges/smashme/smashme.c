#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int helpful() {
  __asm__ ("call %rdi");
}

int main(int argc, char ** argv)
{
    // unbuffered I/O
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    char smashme[64];
    puts("Welcome to the Dr. Phil Show. Wanna smash?\x00\xff\xd7");
    fflush(stdout);
    gets(smashme);

    if(strstr(smashme, "Smash me outside, how bout dAAAAAAAAAAA")) {
        return 0;
    }

    exit(0);
}
