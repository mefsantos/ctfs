#include <stdio.h>


int code = 99;
// my mod to debug it and find the addr of code in the stack

int main() {
    char buf[0x50];
    puts("Hello, big fella! You have one shot!");
    puts("What's your name? ");
    printf("> ");
    fgets(buf, 0x50, stdin);
    printf("Let's see if you are authorized, ");

    printf(buf); // Why not printf("%s", buf) ?

    if (code == 1337) {
        puts("Welcome back, my lord. Enjoy your shell!");
        system("/bin/sh");
    }
    else {
        puts("Nope... Go away!");
    }
    return 0;
}


