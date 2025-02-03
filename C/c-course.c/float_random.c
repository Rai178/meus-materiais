#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    // Seed the random number generator
    srand(time(0));

    // Generate a random dloating-point number between 0.0 and 1.0
    double random_float = (double)rand() / RAND_MAX;
    printf("Random float: %f\n", random_float);

    return 0;
}