#include <stdio.h>

int main() {
    int n, sum, i, j, k;
    int a[100];

    printf("Enter the number of elements: ");
    scanf("%d", &n);

    printf("Enter elements: ");
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);

    printf("Enter the desired sum: ");
    scanf("%d", &sum);

    printf("Triplets with sum %d:\n", sum);

    for (i = 0; i < n - 2; i++) {
        for (j = i + 1; j < n - 1; j++) {
            for (k = j + 1; k < n; k++) {
                if (a[i] + a[j] + a[k] == sum) {
                    printf("(%d, %d, %d)\n", a[i], a[j], a[k]);
                }
            }
        }
    }
    return 0;
}
