#include <stdio.h>


void mergeArray(int arr1[], int arr2[], int arr3[]) {
    int size1 = sizeof(arr1) / sizeof(arr1[0]);
    int size2 = sizeof(arr2) / sizeof(arr2[0]);
    int size3 = sizeof(arr3) / sizeof(arr3[0]);

    int i = 0, j = 0, l = 0;

    while (i < size1) {
        arr3[l++] = arr1[i++];
    }

    // merge sort 
    while (i < size1 && j < size2) {
        if (arr1[i] <= arr2[j]) {
            arr3[l++] = arr1[i++];
        } else {
            arr3[l++] = arr2[j++];
        }
    }

    while (j < size2) {
        arr3[l++] = arr2[j++];
    }


    
}
int main() {

}