#include <stdio.h>

enum TrafficLight {
    RED = 1,
    YELLOW = 2,
    GREEN = 3
};

int main() {
    enum TrafficLight light;

    light = RED;
    printf("Current light: %d\n", light); \\ Output: 1

    if (light == RED) {
        printf("Stop!\n");
    }

    light = GREEN;
    printf("Now the light is: %d\n", light); // Output: 3

    if (light == GREEN) {
        printf("Go!\n");
    }

    return 0;
}