#include <stdio.h>
int main()
{
    int n, m;
    printf("Enter the number of elements in 1st array: ");
    scanf("%d", &n);
    int arr1[n];
    printf("Enter %d elements:\n", n);
    for(int i = 0; i < n; i++)
        scanf("%d", &arr1[i]);
    printf("Enter the number of elements in 2nd array: ");
    scanf("%d", &m);
    int arr2[m];
    printf("Enter %d elements:\n", m);
    for(int i = 0; i < m; i++)
        scanf("%d", &arr2[i]);
    int un[n + m];
    int inter[n < m ? n : m];   
    int k = 0;  
    int l = 0;   
    int found;
    for(int i = 0; i < n; i++)
        un[k++] = arr1[i];
    for(int i = 0; i < m; i++) {
        found = 0;
        for(int j = 0; j < n; j++) {
            if(arr2[i] == arr1[j]) {
                found = 1;
                inter[l++] = arr2[i];   
                break;
            }
        }
        if(found == 0)
            un[k++] = arr2[i];       
    }
    printf("\nUnion of arrays: ");
    for(int i = 0; i < k; i++)
        printf("%d ", un[i]);
    printf("\nIntersection of arrays: ");
    for(int i = 0; i < l; i++)
        printf("%d ", inter[i]);
    return 0;
}
