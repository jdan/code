#include "stdio.h"

void print_str(char *s) {
    if (*s == '\0')
        return;
    write(1, s, 1); // print the first character
    print_str(s+1); // print the rest of the string
}

void rev_str(char *s) {
    if (*s == '\0')
        return;
    rev_str(s+1);   // print the rest of the string
    write(1, s, 1); // print the first character
}

int main(int argc, char **argv) {
    print_str(argv[1]);
    printf("\n");
    rev_str(argv[1]);
    printf("\n");
}