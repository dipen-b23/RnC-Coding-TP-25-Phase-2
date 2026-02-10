#include <stdio.h>

int main() {
    int a[50], b[50], c[100], d[100];
    int n1, n2, i, j, k = 0, l=0;
    int duplicate;

    printf("Enter size of first array: ");
    scanf("%d", &n1);
    printf("Enter elements of first array:\n");
    for(i = 0; i < n1; i++)
        scanf("%d", &a[i]);

    printf("Enter size of second array: ");
    scanf("%d", &n2);
    printf("Enter elements of second array:\n");
    for(i = 0; i < n2; i++)
        scanf("%d", &b[i]);

    for (i=0; i<n1; i++){
        c[k++] = a[i];
    }

    for (i=0; i<n2; i++){
        duplicate = 0;
        for (j=0; j<k; j++){
            if (b[i] == c[j]){
                duplicate = 1;
            }
        }
        if (duplicate){
            d[l++] = b[i];
        }

        if (!duplicate){
            c[k++] = b[i];
        }
    }
    printf ("\nUnion: \n");
    for (i=0; i<k; i++){
        printf ("%d\t", c[i]);
    }
    printf ("\nIntersection: \n");
    for (i=0; i<l; i++){
        printf ("%d\t", d[i]);
    }


}
