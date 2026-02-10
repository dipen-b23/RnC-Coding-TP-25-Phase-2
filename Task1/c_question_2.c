#include<stdio.h>

void selection_sort(int arr[],int low, int n){
    if(low >= n-1 ){
        return;
    }
    int min_index = low;

    for(int i=low+1;i<n;i++){
        if(arr[i] < arr[min_index]){
            min_index = i;
        }
    }
            int temp = arr[low];
            arr[low] = arr[min_index];
            arr[min_index] = temp;
            // low++;

            selection_sort(arr, low+1,n);
}

int main(){
    int n;
    printf("enter length of array: ");
    scanf("%d", &n);

    int arr[n];

    printf("Enter elements of array: ");
    for(int i = 0;i<n;i++){
        scanf("%d", &arr[i]);
    }

    selection_sort(arr, 0,n);

    printf("\nSorted array is: ");
        for(int i = 0;i<n;i++){
        printf("%d\t", arr[i]);
    }

    return 0;
}