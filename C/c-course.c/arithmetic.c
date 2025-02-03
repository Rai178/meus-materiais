#include <stdio.h>

int main() {
    int a = 5;
    int b = 10;

    // Before swap
    printf("Before swap: a = %d, b = %d\n", a, b);

    // Swap values without a temporary variable
    a = a + b; // a becomes 15
    b = a - b; // b becomes 5 (original a)
    a = a - b; // a becomes 10 (original b)

    // After swap
    printf("After swap: a = %d, b = %d\n", a, b);

    return 0;
}