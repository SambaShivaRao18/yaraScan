#include
// Function to swap two elements
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Partition function
int partition(int array[], int low, int high) {
    int pivot = array[high]; // Pivot element
    int i = (low - 1); // Index of smaller element

    for (int j = low; j < high; j++) {
        // If the current element is smaller than or equal to the pivot
        if (array[j] <= pivot) {
            i++; // Increment the index of the smaller element
            swap(&array[i], &array[j]);
        }
    }
    swap(&array[i + 1], &array[high]);
    return (i + 1);
}

// Quick Sort function
void quickSort(int array[], int low, int high) {
    if (low < high) {
        // Partition the array
        int pi = partition(array, low, high);

        // Recursively sort the subarrays
        quickSort(array, low, pi - 1);
        quickSort(array, pi + 1, high);
    }
}

// Function to print an array
void printArray(int array[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

// Main function
int main() {
    int array[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(array) / sizeof(array[0]);
    
    printf("Unsorted array: \n");
    printArray(array, n);

    quickSort(array, 0, n - 1);
    
    printf("Sorted array: \n");
    printArray(array, n);
    
    return 0;
}
 