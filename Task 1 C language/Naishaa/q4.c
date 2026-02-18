#include<stdio.h>
int main(){
    int a[10],b[10],c[20],d[20];
    int n,m,k=0,j=0,p=0,i=0;
    printf("Enter size of first array:");
    scanf("%d",&n);
    printf("Enter elements of first array:");
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
        c[k++]=a[i];
    }   
    printf("Enter size of second array:");
    scanf("%d",&m);
    printf("Enter elements of second array:");
    for(int i=0;i<m;i++){
        scanf("%d",&b[i]);
        //intersecftion
     for (j = 0; j < n; j++) {
            if (b[i] == a[j]) {
                d[p++] = b[i];
                break;
        }
    }
    int flag=0;
    //union
    for(int j=0;j<n;j++){
          if(b[i]==a[j]){
                flag=1;
                break;
            }
        }
            if(flag==0){
            c[k++]=b[i];
        }
    }    
    printf("Union of arrays is: ");
    for(int i=0;i<k;i++){
        printf("%d ",c[i]);
    }
    printf("\nIntersection of arrays is: ");
    for(int i=0;i<p;i++){
        printf("%d ",d[i]);
    }
    return 0;
}
