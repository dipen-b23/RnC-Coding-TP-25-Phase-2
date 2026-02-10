#include <stdio.h>
int main(){
    int n,i,j;
    printf("Enter number of elements: ");
    scanf("%d",&n); 
    int arr[n];
    printf("Enter elements:\n");   
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    printf("Enter the desired sum: ");
    int desired_sum;
    scanf("%d",&desired_sum);
    for(i=0;i<n-2;i++){ 
        for(j=i+1;j<n-1;j++){
            for(int k=j+1;k<n;k++){
                if(arr[i]+arr[j]+arr[k]==desired_sum){
                    printf("Triplet with sum %d: %d, %d, %d\n",desired_sum,arr[i],arr[j],arr[k]);
                }
            }
        }
    }
    return 0;
}