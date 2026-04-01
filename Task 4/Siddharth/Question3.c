
#include <stdio.h>

#define MAX 100

int s1[MAX], s2[MAX];
int t1 = -1, t2 = -1;


void enqueue(int x)
{
    t1++;
    s1[t1] = x;
    printf("Inserted %d\n", x);
}

void dequeue()
{
    if(t1 == -1 && t2 == -1)
    {
        printf("Queue empty\n");
        return;
    }

  
    if(t2 == -1)
    {
        while(t1 != -1)
        {
            t2++;
            s2[t2] = s1[t1];
            t1--;
        }
    }

    printf("Removed %d\n", s2[t2]);
    t2--;
}


void peek()
{
    if(t1 == -1 && t2 == -1)
    {
        printf("Queue is empty\n");
        return;
    }

    if(t2 == -1)
    {
        while(t1 != -1)
        {
            t2++;
            s2[t2] = s1[t1];
            t1--;
        }
    }

    printf("Front is %d\n", s2[t2]);
}

int main()
{
    enqueue(10);
    enqueue(20);
    enqueue(30);

    peek();
    dequeue();
    peek();

    return 0;
}
