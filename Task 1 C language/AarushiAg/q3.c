#include <stdio.h>
int main() {
    int n, sum, i, j, k;
    int arr[50];
    int found = 0;
  
    printf("Enter the no. of elements: ");
    scanf("%d", &n);
    printf("Enter elements: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);}
    printf("Enter sum: ");
    scanf("%d", &sum);
    for (i = 0; i < n - 2; i++) {
        for (j = i + 1; j < n - 1; j++) {
            for (k = j + 1; k < n; k++) {
                if (arr[i] + arr[j] + arr[k] == sum) {
                    printf("Triplets sum %d: (%d, %d, %d)",
                           sum, arr[i], arr[j], arr[k]);
                    found = 1; }}}}
    if (!found) {
        printf("Not found");}
         return 0;}
