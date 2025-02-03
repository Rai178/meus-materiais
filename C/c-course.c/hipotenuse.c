#include <stdio.h>
#include <math.h>

int main(){

    double A;
    double B;
    double C;

    printf("Enter side A:  ");
    scanf("%1f", &A);

    printf("Enter side b: ");
    scanf("%1f", &B);

    C = sqrt(A*A + B*B);

    printf("Side C: %1f", C);

    return 0;
}