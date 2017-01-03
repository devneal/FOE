#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int target;

void win() {
  printf("code execution redirected! you win\n");
  _exit(1);
}

int main(int argc, char **argv) {
  char buffer[512];

  fgets(buffer, sizeof(buffer), stdin);

  printf(buffer);

  exit(1);   
}

