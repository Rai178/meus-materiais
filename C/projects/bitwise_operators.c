#include <stdio.h>

int main()
{
    // BITWISE OPERATORS = special operators used in bit level programming
    //                     (knowing binary is important for this topic)

    // & = AND
    // | = OR
    // ^ = XOR
    // << left shift
    // >> right shift

    int x = 6;   // 6 = 00000110
    int y = 12;  //12 = 00001100
    int z = 0;   // 4 = 00000100

    z = x & y;
    printf("AND = %d\n", z);

    z = x | y;
    printf("OR = %D\n", z);

    z = x ^ y;
    printf("XOR = %d\n", z);

    z = x << 1;
    printf("SHIFT LEFT = %d\n", z);

    z = x >> 1;
    printf("SHIFT RIGHT = %d\n", z);

    return 0;
}