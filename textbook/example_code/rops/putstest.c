#include <stdio.h>

char buf[] = {'h', 'i', 0x04, 't', 'h', 'e', 'r', 'e'};
int main(void) {
    puts(buf);
    return 0;
}
