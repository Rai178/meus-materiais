#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    // Seed the random number generator with the current time
    srand(time(0));

    int random_number = rand();
    printf("Random number: %d\n", random_number);

    return 0;
}