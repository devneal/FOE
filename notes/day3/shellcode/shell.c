#include <unistd.h>

int main(void) {

    char* arg = "/bin/sh";
    char* arg2 = "-p";
    char* end = NULL;
    char *args[] = {arg, arg2, end};
    execve(arg, args, &end);
    return 0;
}
