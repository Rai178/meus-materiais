#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int i;

    // Seed the random number generator
    srand(time(0));

    // Generate and print 5 random numbers between 1 and 50
    for(i = 0; i < 5; i++)
    {
        int random_number = (rand() % 50) + 1;
        printf("Random number %d: %d\n", i+1, random_number);
    }

    return 0;
}