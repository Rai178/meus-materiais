#include <stdio.h>

int main()
{
    //nested loop = a loop inside of another loop

    int rows;
    int columns;
    int i;
    int j;
    char symbol;

    printf("\nEnter # of rows: ");
    scanf("%d", &rows);

    printf("Enter # of columns: ");
    scanf("%d", &columns);

    scanf("%c");

    printf("Enter a symbol to use: ");
    scanf("%c", &symbol);

    for(i = 1; i <= rows; i++)
    {
        for(j = 1; j <= columns; j++)
        {
            printf("%c", symbol);
        }
        printf("\n");
    }

    return 0;
}