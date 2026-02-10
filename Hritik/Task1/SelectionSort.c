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
    
    // Selection Sort Algorithm
    for(i=0;i<n-1;i++){ 
        int min = i;
        for(j=i+1;j<n;j++){
            if(arr[j]<arr[min]){
                min= j;
            }
        }
    
        if(min != i){
            int temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        }
    }
    printf("The largest element is: %d\n",arr[n-1]);
    printf("The smallest element is: %d\n",arr[0]);
    return 0;

}