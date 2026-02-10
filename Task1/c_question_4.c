#include<stdio.h>

int main(){
    int n;
    printf("Enter length of arrays: ");
    scanf("%d", &n);

    int arr1[n];

    printf("Enter elements of array1: ");
    for(int i = 0;i<n;i++){
        scanf("%d", &arr1[i]);
    }

    int arr2[n];

    printf("Enter elements of array2: ");
    for(int i = 0;i<n;i++){
        scanf("%d", &arr2[i]);
    }

    int comm_elements[100];
    int c_e_c = 0;
    int unique_element[100];
    int u_e_c = 0;

    int flag = 0;

    for(int i=0;i<n;i++){


        for(int j=0;j<n;j++){
            if(arr1[i] == arr2[j]){
                comm_elements[c_e_c] = arr1[i];
                c_e_c++;
                flag = 1;    
            }  
        }


        if(flag==0){
            unique_element[u_e_c] = arr1[i];
            u_e_c++;
        }
        flag = 0;


    }

    printf("Common elements are: ");
    for(int i = 0;i<c_e_c;i++){
        printf("%d\t", comm_elements[i]);
    }

        printf("\nUnique elements are: ");
    for(int i = 0;i<n;i++){

        for(int j=0;j<c_e_c;j++){
            if(arr1[i] != comm_elements[j]){
                printf("%d\t", arr1[i]);
            }
            if(arr2[i] != comm_elements[j]){
                printf("%d\t", arr2[i]);
            }
            
        }

    }

}
