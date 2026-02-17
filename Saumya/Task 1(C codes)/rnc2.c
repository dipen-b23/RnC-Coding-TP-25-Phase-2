#include <stdio.h>
int main()
{
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter %d elements: ", n);
    for(int i = 0; i<n; i++)
    {
        scanf("%d", &arr[i]);
    }
    int temp;
    for(int i = 0; i<n-1; i++)
    {
        int pos = i; 
        for(int j = i+1; j<n; j++)
        {
            if(arr[j]<arr[pos])
            {
                pos = j;
            }
        }
        temp = arr[i];
        arr[i] = arr[pos];
        arr[pos] = temp;
    }
    printf("Sorted array:\n");
    for(int k = 0; k<n; k++)
    {
        printf("%d ", arr[k]);
    }
    printf("\nSmallest element in the array is %d\n", arr[0]);
    printf("Largest element in the array is %d", arr[n-1]);
    return 0;
}