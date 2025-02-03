#include <stdio.h>

int main(){

    const double pi = 3.1459;
    double radius;
    double circumference;
    double area;

    printf("\nEnter radius of a circle: ");
    scanf("%1f", &radius);

    circumference = 2 * pi * radius;
    area = pi * radius * radius;

    printf("circumference: %1f", circumference);
    printf("\narea: %1f", area);

    return 0;
}