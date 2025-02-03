#include <stdio.h>

int AND() {
    // compares each bit or two numbers and returns 1 if both bits are 1, otherwise 0.
    int a = 12; // Binary: 1100
    int b = 7; // Binary: 0111
    int result = a & b; // Binary result: 0100 (Decimal: 4)
}

int OR() {
    // compares each bit of two numbers and returns 1 if at least one the bits is 1.
    int a = 12; // Binary: 1100
    int b = 7; // Binary: 0111
    int result = a | b; // Binary result: 1111 (Decimal: 15)
}

int XOR() {
    // compares each bit of two numbers and reuturns 1 if the bits are different, otherwise 0.
    int a = 12; // Binary: 1100
    int b = 7;  // Binary: 0111
    int result = a ^ b; // Binary result: 1011 (Decimal: 11)
}

int NOT() {
    // flips all the bits of the number (0s become 1s, and 1s become 0s).
    int a = 12; // Binary: 0000 1100
    int result = ~a; // Binary result: 1111 0011 (Decimal: -13, int two's complement representation)
}

int LEFT_SHIFT() {
    // Shifts the bits of the number to the left by the specified number of positions. Zeroes are shifted into the vacated positions on the right.
    int a = 5; // Binary: 0000 0101
    int result = a << 1; // Binary result: 0000 1010 (Decimal: 10)
}

int RIGHT_SHIFT(){
    // Shifts the bits of the number to the right by the specified numner of positions
    int a = 20; // Binary: 0001 0100
    int result = a >> 2; // Binary result: 0000 0100 (decimal: 5)
}