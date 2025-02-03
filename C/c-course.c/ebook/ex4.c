# include <stdio.h>

int main()
{
    char pal[10] = {};
    int i = 0;

    printf("digite uma palavra: ");
    scanf("%9s", pal);

    while(i < 10)
    {
        if (pal[i] != '\0')
        printf("informacao: %c e indice: %d\n", pal[i], i);
        else
        printf("informacao truncada: %c e indice: %d\n", pal[i], i);
        i++;
    }
    return 0;
}