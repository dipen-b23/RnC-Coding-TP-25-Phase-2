#include<stdio.h>
int main()
{
    int i,j,n,m,a[100];
    printf("Enter the number of elements in the array");
    scanf("%d",&n);
    int smallest;
    printf("The elements in the array are");
    for(int i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    
        for (i = 0; i < n - 1; i++) {
        smallest = i;

        for (j = i + 1; j < n; j++) {
            if (a[j] < a[smallest]) {
                smallest = j;
            }
        }

        
        int temp = a[i];
        a[i] = a[smallest];
        a[smallest] = temp;
        }

        printf("The largest element is %d\n",a[n-1]);
        printf("The smallest element is %d\n",a[0]);
        
        return 0;
        
}
