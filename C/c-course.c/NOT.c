#include <stdio.h>
#include <stdbool.h>

int main(){

    // logical operators = ! (NOT) reverses the state of a condition

    bool sunny = false;

    if(!sunny){
        printf("\nIt's cloudy outside!");
    }
    else{
        printf("\nIt's sunny outside!");
    }
}