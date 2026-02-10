#include<stdio.h>
int main()
{
    int n,a[10];
    printf("Enter the size:");
    scanf("%d",&n);
    printf("\nEnter the elements of array:");
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    int  pos ,small,large,temp;
    for(int i=0;i<n-1;i++){
        pos=i;
        for(int j=i+1;j<n;j++){
            if(a[j]<a[pos]){
                pos=j;
            }
        temp=a[i];
        a[i]=a[pos];
        a[pos]=temp;
        }
        
    }
    printf("\nSorted array is:");
    for(int k=0;k<n;k++){
        printf("%d\t",a[k]);
    }   
    printf("\nSmallest element is %d",a[0]);
    printf("\nLargest element is %d",a[n-1]);
}