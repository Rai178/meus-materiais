#include <stdio.h>

int main() {
    int a = 5;
    int b = 10;

    // Before swap
    printf("Before swap: a = %d, b = %d\n", a, b);
    
    
    // Swap using XOR bitwise operation
    a = a ^ b; // XOR of a and b
    b = a ^ b; // b becomes original a 
    a = a ^ b; // a becomes original b

    // After swap
    printf("After swap: a = %d, b = %d\n", a, b);

    return 0;
}