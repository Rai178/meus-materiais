#include <stdio.h>

int main()
{
    int vet[4];
    int i;
    i = 0;
    while (i <= 3)
    {
        printf("digite o numero:\n");
        scanf("%d", &vet[i]);
        i++;
    }
    i = 0;
    while (i <= 3)
    {
        printf("numero %d\n", vet[i]);
        i++;
    }
}