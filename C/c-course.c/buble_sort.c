#include <stdio.h>
int i;
int j;
void bubbleSort(int array[], int size) {
    for ( i = 0; i < size - 1; i++) {
        for ( j = 0; j < size - i - 1; j++) {
            if (array[j] > array[j + 1]) {
                // Swap the elements
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp; 
            }
        }
    }
}

void printArray(int array[], int size) {
    for ( i = 0; i < size; i++){
        printf("%d ", array[i]);
    }
    printf("\n");
}

int main() {
    int data[] = {5, 2, 9, 1, 5, 6};
    int size = sizeof(data) / sizeof(data[0]);
    

    printf("Unsorted array: \n");
    printArray(data, size);

    bubbleSort(data, size);

    printf("Sorted array in ascending order: \n");
    printArray(data, size);

    return 0;
}