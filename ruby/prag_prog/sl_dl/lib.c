#include <stdio.h>
int print_msg(char *text, int number) {
  int count = printf("Text: %s (%d)\n", text, number);
  fflush(stdout);
  return count;
}
