#include<stdio.h>
 int main()
{
    int i,j;
    for(i=1;i<=5;i++){
        for(j=4;j>=i;j--){
            printf("\t");
        }
        for(int k=1;k<=i;k++){
            printf("*\t");
        }
        printf("\n");
    }
    return 0;
}