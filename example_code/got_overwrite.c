#include <stdio.h>
#include <stdlib.h>

int main()
{
    unsigned long long int cards[8] = {10, 7, 5, 8, 4, 6, 9, 5};
	char buf[32];
    int cardNum;
	puts("Welcome to FOE Corp.");
	puts("Please take a card and sign in with your name.");
	puts("We've installed a canary to foil your overflows. There's no way you can hack us now!");
    printf("Choose a card:\n");
    fgets(buf, 64, stdin);
    cardNum = atoi(buf);
    printf("You're customer number %llu. What's your name?\n", cards[cardNum]);
	gets(buf);
	puts("Please take a seat, we'll be with you at some point this week.");
	return 0;
}
