#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

unsigned int num_nums;

void read_nums(unsigned char* nums, unsigned int size)
{
	num_nums = 0;
	for (int i = 0; i < size; i++)
	{
		printf("Please enter number number %d: ", i+1);
		int ret = scanf("%hhu", &nums[i]);
		if (ret != 1)
		{
			printf("Fine, don't enter a number. But you're not taking full advantage of our awesome technology...\n");
			break;
		}
		num_nums++;
	}
}

void sort(unsigned char* nums)
{
	printf("Please sort by entering the two indexes to swap\n");
	int a, b;
	while (1)
	{
		int ret = scanf("%d %d", &a, &b);
		if (ret != 2)
			break;
		if (a < 0 || a > num_nums || b < 0 || b > num_nums)
			printf("Are you daft? That's not a valid index!\n");
		else
		{
			int tmp = nums[a];
			nums[a] = nums[b];
			nums[b] = tmp;
		}
	}
	printf("Alright, let's check your work...\n");
	for (int i = 1; i < num_nums; i++)
		if (nums[i] < nums[i-1])
		{
			printf("Bah! Did you think I wouldn't realize %hhu is less than %hhu??\n", nums[i], nums[i-1]);
			exit(-1);
		}
}

void print_nums(unsigned char* nums)
{
	for (int i = 0; i < num_nums; i++)
		printf("%hhu ", nums[i]);
	printf("\n");
}

void take_tour()
{
	unsigned char nums[16];
	memset(nums, 0, sizeof(nums));
	printf("Our newest exhibit has you sort up to 16 numbers, compare that to 8 last year!\n");
	read_nums(nums, sizeof(nums));
	if (!num_nums)
	{
		printf("I really am quite offended....\n");
		exit(-1);
	}
	printf("Now let's see if you're smart enough to sort those numbers.\n");
	printf("Here they are again: ");
	print_nums(nums);
	sort(nums);
	printf("Wow, you're sorting skills are phenomenal! Be sure to come back next year when we're surt to have a 32 number sorting exhibit!\n");
}

int main()
{
	setvbuf(stdout, 0, _IONBF, 0);
	char name[0x100];
	memset(name, 0, sizeof(name));
	printf("Welcome young traveler!\n");
	printf("This here's a sorting emporium, so let's get your stuff in order ;)...\n");
	printf("Please record your name in the guest book: ");
	int ret = read(0, name, sizeof(name)-1);
	if (ret <= 0)
	{
		printf("I'm sorry, we unfortunately discriminate against those with no names...\n");
		exit(-1);
	}
	char* nline = strchr(name, '\n');
	if (nline)
		*nline = 0;
	printf("Welcome %s to the finest sorting establishment in all of userspace!\n", name);
	printf("Enjoy the tour! Or not, I get paid either way.\n");
	take_tour();
}
