#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    int ans = 0;
    int target = atoi(argv[1]);
    for (int i = 0; i <= target; i++)
        ans += i;
    printf("%d\n", ans);
}
