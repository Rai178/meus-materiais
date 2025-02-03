#include <stdio.h>

int main()
{
    int lin, col;
    int mat[4][4];
    
    for (lin = 0; lin < 4; lin++)
    {
        for (col = 0; col < 4; col++)
        {
            printf("digite o elemento da linha %d, colula %d da matriz:", lin + 1, col + 1);
            scanf("%d", &mat[lin][col]);
        }
    }

    printf("matriz\n");
    for (lin = 0; lin < 4; lin++)
    {
        for (col = 0; col < 4; col++)
        {
            printf("%d\t", mat[lin][col]);
        }
        printf("\n");
    }

    return 0;
}