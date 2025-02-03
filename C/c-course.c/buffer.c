#include <stdio.h>

int main()
{
    int age;
    char name[1024];

    // stdin: \n
    printf("Enter Age: ");
    scanf("%d", &age);

    printf("Enter name: ");
    fgets(name, 1024, stdin);

    printf("Age: %d\n", age);
    printf("Name: %s\n", name);

    return 0;
}