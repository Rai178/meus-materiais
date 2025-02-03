#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    const int MIN = 100;
    const int MAX = 1000;
    int guess;
    int guesses;
    int answer;

    //uses the current time as a seed
    srand(time(0));

    //generate a random number between MIN & MAX
    answer = (rand() % MAX) + MIN;
    guesses = 0;

    do{
        printf("Enter a guess: ");
        scanf("%d", &guess);
        if(guess > answer)
        {
            printf("Too high!\n");
        }
        else if(guess < answer)
        {
            printf("Too low!\n");
        }
        else{
            printf("CORRECT!\n");
        }
        guesses++;
    }while(guess != answer);

    printf("**********************\n");
    printf("answer: %d\n", answer);
    printf("guesses: %d\n", guesses);
    printf("*************************\n");

    
    return 0;
}