#include <stdio.h>

int main(){
    // Declare and initalize an array of integers
    int numbers[5] = {10, 20, 30, 40, 50};
    int i;

    // Modify an element
    numbers[2] = 35;

    // Loop though the array and print its elements
    for (i = 0; i < 5; i++) {
        printf("Element at index %d: %d\n", i, numbers[i]);
    }

    // Accessing out-of-bounds (causes undefined behavior)
    // printf("Out-of-bounds access: %d\n", numbers[10]);

    return 0;
}