#include <stdio.h>
int main() {
    int n, i, j, mIndex, temp;
    int arr[50];
    printf("Enter the no. of elements: ");
    scanf("%d", &n);
    printf("Enter elements: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);}
    for (i = 0; i < n - 1; i++) {
        minIndex = i;
        for (j = i + 1; j < n; j++) {
            if (arr[j] < arr[mIndex]) {
                mIndex = j;}}
        temp = arr[i];
        arr[i] = arr[mIndex];
        arr[mIndex] = temp;
    }
    printf("Max element: %d", arr[n - 1]);
    printf("Min element: %d", arr[0]);
    return 0;}
