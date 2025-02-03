#include <stdio.h>

int main() {
    int a = 5;
    int b = 3;
    int temp;  // Declare a temporary variable

    printf("Before swap: a = %d, b = %d\n", a, b);

    // Swapping process
    temp = a; // Store the value of 'a' in 'temp'
    a = b;    // Assing the value of 'b' to 'a'
    b = temp; // Assign the value of 'temp' (old value of 'a') to 'b'

    printf("After swap: a = %d, b = %d\n", a, b);

    return 0;
}