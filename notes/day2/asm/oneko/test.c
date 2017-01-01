#include <stdio.h>
#include <unistd.h>

int main(void) {
    char* filename = "/usr/games/oneko";

    char* arg1 = filename;
    char* arg2 = "-sakura";
    char* argv[] = {arg1, arg2, 0x0};

    char* env1 = "DISPLAY=:0";
    char* envp[] = {env1, 0x0};

    execve(filename, argv, envp);

    return 0;
}
