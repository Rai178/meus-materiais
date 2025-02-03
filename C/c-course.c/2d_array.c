#include <stdio.h>

int main()
{
    // 2D array = an array, where each element is an entire array
    //            useful id you need a matrix, grid, or table of data

    /*
    int numbers[2][3] = {
        {1, 2, 3}, 
        {4, 5, 6};
    };
    */
   int j;
   int i;
   int rows = sizeof(numbers)/sizeof(numbers[0]);
   int columns = sizeof(numbers)/sizeof(numbers[0][0]);
   int numbers[3][3];

   numbers[0][0] = 1;
   numbers[0][1] = 2;
   numbers[0][2] = 3;
   numbers[1][0] = 4;
   numbers[1][1] = 5;
   numbers[1][2] = 6;

    for(i = 0; i < rows; i++)
    {
        for (j = 0; j < columns; j++)
        {
            printf("%d", numbers[i][j]);
        }
        printf("\n");
    }

    return 0;
}