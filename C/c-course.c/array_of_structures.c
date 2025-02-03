#include <stdio.h>

struct Person 
{
    char name[50];
    int age;
    float height;
};

int main() {
    struct Person people[2];
    int i;
    for(i = 0; i < 2; i++) {
        printf("Enter details for person %d\n", i + 1);
        printf("Enter name: ");
        fgets(people[i].name, sizeof(people[i].name), stdin);
        printf("Enter age: ");
        scanf("%d", &people[i].age);
        printf("Enter height: ");
        scanf("%f", &people[i].height);
        getchar(); // To consume the newline left by scanf
    }

    for (i = 0; i < 2; i++) {
        printf("\nPerson %d\n", i + 1);
        printf("Name: %s", people[i].name);
        printf("Age: %d\n", people[i].age);
        printf("Height: %.2f\n", people[i].height);
    }

    return 0;
}