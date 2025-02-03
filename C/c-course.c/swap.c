#include <stdio.h>

int main() {
    int a = 5;
    int b = 10;
    int temp; // Temporary variable

    // Before swap
    printf("Before swap: a = %d, b = %d\n", a, b);

    // Swap values
    temp = a;  // Store the value of 'a' in 'temp'
    a = b;     // Assign the value of 'b' to 'a'
    b = temp;  // Assign the value stored in 'temp' (original 'a') to 'b'

    // After swap
    printf("After swap: a = %d, b = %d\n", a, b);

    return 0;
}