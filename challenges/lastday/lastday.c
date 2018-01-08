#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define NUM_NOTES 5
#define NOTE_SIZE 16

struct day {
   char* title;
   char* when;
   char* description;
   char notes[NUM_NOTES][NOTE_SIZE];
   struct day* next;
};

struct day day0 = {
   .title = "Linux, ELF, and RE",
   .when = "Jan/08 Mon 01:00PM-04:00PM NE 45 2nd Floor",
   .description = "This session will cover ELF binaries, "
                  "the programs we'll be working with for the rest of the course.\n"
                  "We'll learn how C programs are converted into ELFs and "
                  "learn the basics of assembly, the language that ELFs are written in.\n"
                  "Then we'll go over the way the stack is used in function calls, and "
                  "how to use GDB to inspect ELF binaries as they execute.",
   .notes = {"", "", "", "", ""},
   .next = NULL
};

struct day day1 = {
   .title = "Fundamentals of PWN",
   .when = "Jan/09 Tue 01:00PM-04:00PM NE 45 2nd Floor",
   .description = "Once we've got some familiarity with ELF binaries, "
                  "we can get started on basic exploits.\n"
                  "We'll find out how to exploit unsafe functions to corrupt memory, "
                  "call other functions, and eventually get shell access via shellcoding.\n"
                  "We'll also go over ret2libc, "
                  "a technique to get shell access without writing shellcode.",
   .notes = {"", "", "", "", ""},
   .next = &day0
};

struct day day2 = {
   .title = "DEP, ROP, and ASLR",
   .when = "Jan/10 Wed 01:00PM-04:00PM NE 45 2nd Floor",
   .description = "This session will introduce data execution prevention (DEP) and "
                  "return-oriented programming (ROP), which is used to defeat it.\n"
                  "We will also cover ASLR and and "
                  "the way it is typically defeated via memory leaks.",
   .notes = {"", "", "", "", ""},
   .next = &day1
};

struct day day3 = {
   .title = "Stack Canaries, GOT/PLT, and RELRO",
   .when = "Jan/11 Thu 01:00PM-04:00PM NE 45 2nd Floor",
   .description = "During this session we'll learn about stack canaries, "
                  "another mitigation technique against stack smashing.\n"
                  "Then we'll go over the global offset table (GOT) and "
                  "procedure linkage table (PLT), and "
                  "how they can be used to take control of a program.\n"
                  "We will also learn about RELRO, "
                  "a mitigation technique to prevent this type of exploit.",
   .notes = {"", "", "", "", ""},
   .next = &day2
};

struct day day4 = {
   .title = "Miscellaneous",
   .when = "Jan/12 Fri 01:00PM-04:00PM NE 45 2nd Floor",
   .description = "This session will cover less widely-used exploit techniques and "
                  "allow you to gain more experience with the ones you already learned.",
   .notes = {"", "", "", "", ""},
   .next = &day3
};

int num_days = 4;
struct day* last_day = &day4;


struct day *get_day(int n)
{
   struct day* ptr = last_day;
   int i = num_days;
   while (i > n) {
      ptr = ptr->next;
      i--;
   }
   return ptr;
}

int get_digit(int max)
{
   int n = getchar() - '0';
   while(getchar() != '\n');
   if (n > 9 || n > max) {
      printf("Invalid input (%d)\n", n);
      exit(-1);
   }
   return n;
}

void read_note()
{
   int day, index;

   printf("Enter day #\n$ ");
   day = get_digit(num_days);
   printf("Entered day %d\n", day);

   printf("Enter note #\n$ ");
   index = get_digit(NUM_NOTES);
   printf("Entered note %d\n", index);

   printf("note %d %d: %s\n", day, index, get_day(day)->notes[index]);
}

void take_note()
{
   char note[sizeof(((struct day*)0)->notes)];
   int day;
   int index;

   printf("Enter day #\n$ ");
   day = get_digit(num_days);
   printf("Entered day %d\n", day);

   printf("Enter note #\n$ ");
   index = get_digit(NUM_NOTES);
   printf("Entered note %d\n", index);

   printf("Enter note contents\n");
   if (gets(note) == NULL) {
      printf("fgets failed\n");
      exit(-1);
   }
   printf("Entered note: %s\n", note);
   strncpy(get_day(day)->notes[index], note, NOTE_SIZE);
}

void add_day()
{
   struct day* new_day = (struct day*) malloc(sizeof(struct day));
   char* title = malloc(20);
   char* when = malloc(20);
   char* description = malloc(200);


   printf("Enter title\n$ ");
   if (gets(title) == NULL) {
      printf("fgets failed\n");
      exit(-1);
   }
   printf("Enter when\n$ ");
   if (gets(when) == NULL) {
      printf("fgets failed\n");
      exit(-1);
   }
   printf("Enter description\n$ ");
   if (gets(description) == NULL) {
      printf("fgets failed\n");
      exit(-1);
   }
   new_day->title = title;
   new_day->when = when;
   new_day->description = description;
   new_day->next = last_day;
   last_day = new_day;
   num_days++;

   printf("Day %u - %s\n===================================================\n"
          "[+] %s\n%s\n\n Notes:\n%s\n%s\n%s\n%s\n%s\n",
          num_days, get_day(num_days)->title,
          get_day(num_days)->when, get_day(num_days)->description,
          get_day(num_days)->notes[0],
          get_day(num_days)->notes[1],
          get_day(num_days)->notes[2],
          get_day(num_days)->notes[3],
          get_day(num_days)->notes[4]);
}

void (*menu_options[3])() = {
   take_note,
   read_note,
   add_day,
};

void menu()
{
   int choice;

   do {
      printf("MENU:\n\n0) exit\n1) take note\n2) read note\n3) add day\n$ ");
      choice = get_digit(4);
      if (choice != 0) {
         menu_options[choice - 1]();
      }
   } while (choice != 0);
}

int main(int argc, char* argv[])
{
   unsigned i;
   // unbuffered I/O
   setvbuf(stdin, NULL, _IONBF, 0);
   setvbuf(stdout, NULL, _IONBF, 0);

   for (i=0; i < 5; ++i) {
      printf("Day %u - %s\n===================================================\n"
             "[+] %s\n%s\n\n Notes:\n%s\n%s\n%s\n%s\n%s\n",
             i, get_day(i)->title, get_day(i)->when, get_day(i)->description,
             get_day(i)->notes[0],
             get_day(i)->notes[1],
             get_day(i)->notes[2],
             get_day(i)->notes[3],
             get_day(i)->notes[4]);
   }

   menu();

   return 0;
}
