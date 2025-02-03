#include <stdio.h>

int main(){

    int age;

    printf("\nEnter your age: ");
    scanf("%d", &age);

    if(age >= 18){
        printf("Your are now signed up!");
    }
    else if(age == 0){
        printf("Your can't sign up! You were just born!");
    }
    else if(age < 0){
        printf("Your haven't been born yet!");
    }
    else{
        printf("You are too young to sign up!");
    }
}