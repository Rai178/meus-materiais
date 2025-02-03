#include <stdio.h>
int main()
{
    int lin, col;
    int mat[3][3], mat1[3][3];
    for (lin = 0; lin < 3; lin++)
    {
        for (col = 0; col < 3; col++)
        {
            printf("digite ELEMENTO da linha %d, coluna %d da matriz: ", lin + 1, col + 1);
            scanf("%d", &mat[lin][col]);
        }
    }

    printf("matriz original\n");
    for (lin = 0; lin < 3; lin++)

    {
        for (col = 0; col < 3; col++)
        {
            printf("%d\t", mat[lin][col]);
            
        }
        printf("\n");
    }

    for (lin = 0; lin < 3; lin++)
    {
        for (col = 0; col < 3; col++)
            mat1[lin][col] = mat[lin][col]*2;
    }

    printf("\n\nmatriz com elementos multiplicados por 2\n\n");
    for (lin = 0; lin < 3; lin++)
    {
        for(col = 0; col < 3; col++)
        {
            printf("%d\t", mat1[lin][col]);
            
        }
        printf("\n");
    }   

    

    return 0;

}