#include <stdio.h>

int main()
{
    int x = 42;
    int *p = &x;

    printf("valor de x: %d\n", x);
    printf("endereco de x: %p\n", &x);
    printf("valor de p (endereco de x): %p\n", p);
    printf("valor apontado por p: %d\n", *p);

    return 0;
}