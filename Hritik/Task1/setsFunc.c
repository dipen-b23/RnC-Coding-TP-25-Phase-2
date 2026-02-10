#include <stdio.h>
int main(){
    int n1,n2,i,j;
    printf("Enter number of elements in array 1: ");
    scanf("%d",&n1); 
    int arr1[n1];
    printf("Enter elements:\n");   
    for(i=0;i<n1;i++){
        scanf("%d",&arr1[i]);
    }

    printf("Enter number of elements in array 2: ");
    scanf("%d",&n2); 
    int arr2[n2];
    printf("Enter elements:\n");   
    for(i=0;i<n2;i++){
        scanf("%d",&arr2[i]);
    }
    printf("Intsection:\t");
    for(i=0;i<n1;i++){ 
        for(j=0;j<n2;j++){
            if(arr1[i]==arr2[j]){
                printf("%d ",arr1[i]);
            }
        }
    }
    printf("Union:\t");
    for(i=0;i<n1;i++){ 
        printf("%d ",arr1[i]);
    }
    for(i=0;i<n2;i++){
        int flag=0;
        for(j=0;j<n1;j++){
            if(arr2[i]==arr1[j]){
                flag=1;
                break;
            }   
        }
        if(flag==0){
            printf("%d ",arr2[i]);
        }
    }
}