#include <stdio.h>

// Define a new name for 'unsigned int'
typedef unsigned int uint;

int main() {
    uint age = 30; // 'uint' is now an alias for 'unsigned int'
    printf("Age: %u\n", age);

    return 0;
}