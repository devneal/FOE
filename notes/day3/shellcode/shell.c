#include <unistd.h>
#include <stdlib.h>

int main(void) {

    // Testing execve()
    char* arg = "/bin/sh";
    char* arg2 = "-p";
    char* end = NULL;
    char *args[] = {arg, arg2, end};
    execve(arg, args, &end);

    /**
    // Testing system()
    setuid(0);
    system("/bin/sh");
    **/
    return 0;
}
