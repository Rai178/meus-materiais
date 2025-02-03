#include <stdio.h>

int main()
{
   int lixo[10] = {}
   int indice = 0;
   while (indice < 10)
   {
    printf("lixo na posicao %d: %d\n", indice, lixo[indice]);
    indice++;
   }
}