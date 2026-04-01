
#include <stdio.h>

int main() {
    
    int arr[] = {2, 4, 7, 1, 5, 3};
    int sum = 10;

    int n = 6;
    int i, j, k;
    int found = 0;

    for(i = 0; i < n; i++) {
        for(j = i + 1; j < n; j++) {
            for(k = j + 1; k < n; k++) {

                if(arr[i] + arr[j] + arr[k] == sum) {
                    printf("Triplet found: %d, %d, %d\n", arr[i], arr[j], arr[k]);
                    found = 1;
                }

            }
        }
    }

    if(found == 0) {
        printf("No triplet found");
    }

    return 0;
}
