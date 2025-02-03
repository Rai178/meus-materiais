#include <stdio.h>

int main()
{
    // while loop = checks a condition, THEN executes a block of cod if condition is true
    // do while loop = always executes a block of code onde, THEN checks a condition

    int number = 0;
    int sum = 0;

   
    do{
        printf("Enter a # above 0:  ");
        scanf("%d", &number);
        if(number > 0)
        {
            sum += number;
        }
    }while(number > 0);

    printf("sum:  %d", sum);

    return 0;

    // the key differences:
    // condition check timing:
    // while: first check the condition, befote the loop is executed
    // do-while: first execute one time the loop, then check if the condition is true.

}