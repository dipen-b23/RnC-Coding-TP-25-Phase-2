#include <stdio.h>

int main() {
    int a[100], b[100], u[200], inter[100];
    int n1, n2, i, j, k = 0, m = 0, found;

    printf("Enter the number of elements in first array: ");
    scanf("%d", &n1);
    printf("Enter elements of first array: ");
    for (i = 0; i < n1; i++)
        scanf("%d", &a[i]);

    printf("Enter the number of elements in second array: ");
    scanf("%d", &n2);
    printf("Enter elements of second array: ");
    for (i = 0; i < n2; i++)
        scanf("%d", &b[i]);

    // Union
    for (i = 0; i < n1; i++)
        u[k++] = a[i];

    for (i = 0; i < n2; i++) {
        found = 0;
        for (j = 0; j < n1; j++) {
            if (b[i] == a[j]) {
                found = 1;
                break;
            }
        }
        if (!found)
            u[k++] = b[i];
    }

    // Intersection
    for (i = 0; i < n1; i++) {
        for (j = 0; j < n2; j++) {
            if (a[i] == b[j]) {
                inter[m++] = a[i];
                break;
            }
        }
    }

    printf("Union: ");
    for (i = 0; i < k; i++)
        printf("%d ", u[i]);

    printf("\nIntersection: ");
    for (i = 0; i < m; i++)
        printf("%d ", inter[i]);

    return 0;
}
