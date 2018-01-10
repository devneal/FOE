#include <stdio.h>
#include <unistd.h>

void trfghy(int len) {
  puts("read");
  printf("%d\n", len);
  char buf[100];
  read(STDIN_FILENO, buf, len);
  return;
}

int main() {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  puts("see if you can call /bin/sh");
  trfghy(144);
  puts("goodbye");
  return 0;
}
