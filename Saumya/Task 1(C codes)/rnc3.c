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
    int num;
    printf("Enter the desired sum: ");
    scanf("%d", &num);
    int n1, n2, n3;
    int found= 0;
    for(int i =0; i<n; i++)
    {
        for(int j = i+1; j<n; j++)
        {
            for(int k = j+1; k<n; k++)
            {
                if(arr[i]+arr[j]+arr[k]==num)
                {
                    found = 1;
                    n1 = arr[i];
                    n2 = arr[j];
                    n3 = arr[k];
                    break;
                }
            }
        }
    }
    if(found)
    {
        printf("Triplets with sum %d: (%d,%d,%d)", num,n1,n2,n3);
    }
    else
        printf("No triplets found from array");
    return 0;
}