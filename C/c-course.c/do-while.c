#include <stdio.h>

int main() {
    int count = 0;

    do {
        printf("do-while loop: count = %d\n", count);
        count++;
    } while(count < 3);

    return 0;
}