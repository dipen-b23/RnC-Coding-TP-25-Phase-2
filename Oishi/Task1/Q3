#include <stdio.h>
int triplet (int a[], int tar, int n){
    int i, j,k, found=0;
    for (i=0; i<n; i++){
        for (j=i+1; j<n; j++){
          
            for (k=j+1; k<n; k++){
                    if (a[i]+a[j]+a[k] == tar){
                        printf ("(%d %d %d)\n", a[i], a[j], a[k]);
                        found =1;
                    }
                }            
            
        }
    }
    if (!found) {
        printf("No triplets found\n");
    }
}
int main (void){
    int n, min, i,j, tar;
    int a[100];
    printf ("Enter the number of elements: ");
    scanf ("%d", &n);
    printf ("\nEnter the elements: ");
    for (i=0; i<n; i++){
        scanf ("%d", &a[i]);
    }
    printf ("\nEnter target sum: ");
    scanf ("%d", &tar);
    triplet (a, tar, n);
   
}
