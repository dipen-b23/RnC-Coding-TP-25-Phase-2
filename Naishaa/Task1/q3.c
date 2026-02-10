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
    int sum;
    printf("Enter the sum:");
    scanf("%d",&sum);
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            for(int k=j+1;k<n;k++){
            if(a[i]+a[j]+a[k]==sum){
                printf("triplets are:(%d,%d,%d)\n",a[i],a[j],a[k]);
            }
            else{
                printf("No triplets found\n");
            }
        }
    }
}
else{
                printf("No triplets found\n");
            }
return 0;
}