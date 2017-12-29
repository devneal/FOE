#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>

int fd = 0;
char data[256];


void ret(int a) {
  if (a == 0xbadbeef) {
    fd = open("flag.txt", O_RDONLY);
    puts("[+] open\n");
    fflush(stdout);
  }
  else {
    puts("Wrong key :(\n");
    exit(0);
  }
}

void ori(int b, int c) {
  if (b == 0xabcdefff || c == 0x78563412) {
    read(fd, data, 128);
    puts("[+] read\n");
    fflush(stdout);
  } else {
    puts("Wrong key :((\n");
    exit(0);
  }
  return;
}

void pro() {
  puts("[+] print\n");
  fflush(stdout);
  printf("%s", data);
  fflush(stdout);
  return;
}

void ezy() {
  puts("Welcome to the RetOriPro conference!\nWould you like to leave a message?");
  fflush(stdout);
  char buffer[40];
  read(STDIN_FILENO, buffer, 64);
  return;
}

int main() {
  ezy();
  puts("goodbye!\n");
  return 0;
}
