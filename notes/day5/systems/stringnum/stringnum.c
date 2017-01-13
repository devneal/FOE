#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>

char* s = "refe_iz_cool";

void shell(void) {
    system("cat ./flag.txt");
}

int main(int argc, char** argv) {
    unsigned int arr[4];

    int last_idx;
    if (argc < 4)
        last_idx = argc;
    else
        last_idx = 4;

    for (int i=1; i<last_idx; i++)
        sscanf(argv[i], "%u", &arr[i-1]);

    arr[3] = 0;

    if (strcmp((char *)arr, s) == 0)
        shell();
    else
        printf("Try again...\n");
}
