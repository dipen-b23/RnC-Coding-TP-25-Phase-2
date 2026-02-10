#include <stdio.h>
int main (void){
    int n, min, i,j, temp;
    int a[100];
    printf ("Enter the number of elements: ");
    scanf ("%d", &n);
    printf ("\nEnter the elements: ");
    for (i=0; i<n; i++){
        scanf ("%d", &a[i]);
    }

    for (i=0; i<n-1; i++){
        min = i;
        for (j=i+1; j<n; j++){
            if (a[j]<a[min]){
                min = j;
            }
        }
        int temp = a[min];
        a[min] = a[i];
        a[i] = temp;
    }
    for (i=0; i<n; i++){
        printf ("%d\t", a[i]);
    }
    printf ("\nSmallest element: %d", a[0] );
    printf ("\nLargest element: %d", a[n-1] );
}
