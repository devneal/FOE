/* Defeated by using the leak to bypass ASLR, then using ret2libc/ROP */
#include <stdio.h>
#include <stdlib.h>

int main()
{
	char name[32];
	puts("Welcome to FOE Corp.");
	puts("Please sign in with your name.");
    printf("By the way, I found this on the floor. Is it yours? %p\n", *(long long int*)*(*(int*)*(puts+2)+(puts+6)));
	gets(name);
	printf("Please take a seat, we'll be with you at some point this week.\n");
	return 0;
}
