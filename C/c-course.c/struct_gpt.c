#include <stdio.h>

// Define structure
struct Person {
    char name[50];
    int age;
    float height;
};

int main() {
    // Declare a variable of type 'struct Person'
    struct Person person1;

    // Assing values to members of 'person1'
    printf("Enter name: ");
    fgets(person1.name, sizeof(person1.name), stdin);

    printf("Enter age: ");
    scanf("%d", &person1.age);

    printf("Enter height: ");
    scanf("%f", &person1.height);

    // Access and display the values
    printf("\nName: %s", person1.name);
    printf("Age: %d\n", person1.age);
    printf("Height: %.2f\n", person.height);

    return 0;
}