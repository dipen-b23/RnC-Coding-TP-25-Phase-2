
#include<stdio.h>
int main()
{
    int i,j,a[100],b[100];
    int n,m;
    printf("Enter the number of element in the 1st array \n");
    scanf("%d",&n);
    printf("Enter the elements\n");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }

    printf("Enter the number of element in the 2nd array \n");
    scanf("%d",&m);
    printf("Enter the elements\n");
    for(i=0;i<m;i++)
    {
        scanf("%d",&b[j]);
    }
    printf("The intersection is\n ");
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            if(a[i]==b[j])
            printf("%d\t",a[i]);
        }
    }

    printf("The union is \n");
    for(i=0;i<n;i++)
    {
        printf("%d\t",a[i]);
    }
    for(j=0;j<m;j++)
    {
        int flag=0;
        for(i=0;i<n;i++)
        {
            if(a[i]==b[j]){
                flag=1;
                break;
            }
        }

        if(flag=0)
        {
            printf("%d\t",b[j]);
        }
    }

    return 0;
}
