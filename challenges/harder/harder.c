#include <stdio.h>
#include <unistd.h>

void trfghy(int len) {
  puts("read");
  printf("%d\n", len);
  fflush(stdout);
  char buf[100];
  read(STDIN_FILENO, buf, len);
  return;
}

int main() {
  puts("no easy string for you");
  trfghy(144);
  puts("goodbye");
  return 0;
}
