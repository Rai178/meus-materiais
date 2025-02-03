#include <stdio.h>

// Define an enumeration for days of the week
enum Weekday {
    SUNDAY,
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURDAY,
    FRIDAY,
    SATURDAY
};

int main(){
    // Declare a variable of type enum Weekday
    enum Weekday today;

    // Assign a value to 'today'
    today = WEDNESDAY;

    // Print the value of 'today'
    printf("Day number: %d\n", today);

    if (today == WEDNESDAY) {
        printf("It's the middle of the week!\n");
    }

    return 0;
}