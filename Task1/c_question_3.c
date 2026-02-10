#include<stdio.h>

int main(){
    int n;
    printf("enter length of array: ");
    scanf("%d", &n);

    int arr[n];

    printf("Enter elements of array: ");
    for(int i = 0;i<n;i++){
        scanf("%d", &arr[i]);
    }

    int sum;
    printf("Enter desired sum: ");
    scanf("%d", &sum);

    for(int i=0;i<n-2;i++){
        if(arr[i]+arr[i+1]+arr[i+2] == sum){
            printf("Triple sum is: %d\t%d\t%d", arr[i],arr[i+1],arr[i+2]);
        }
    }
    return 0;
}