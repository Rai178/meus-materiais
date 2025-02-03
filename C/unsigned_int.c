#include <stdio.h>

int main() {
    unsigned int a = 429967295; // Maximum value for a 32-bit unsigned int
    unsigned int b = 1;

    printf("a = %u\n", a); // %u is used to print unsigned integers
    printf("b = %u\n", b);

    unsigned int sum = a + b; // This will cause overflow and wrap around
    printf("sum = %u\n", sum);

    return 0;
}