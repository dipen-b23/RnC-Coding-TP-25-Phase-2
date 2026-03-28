#include <stdio.h>
#define MAX 100

int s1[MAX], s2[MAX];
int top1 = -1, top2 = -1;

void push1(int x)
{
    s1[++top1] = x;
}

void push2(int x)
{
    s2[++top2] = x;
}

int pop1()
{
    return s1[top1--];
}

int pop2()
{
    return s2[top2--];
}

void enqueue(int x)
{
    push1(x);
}

void transfer()
{
    if (top2 == -1)
    {
        while (top1 != -1)
            push2(pop1());
    }
}

int dequeue()
{
    transfer();
    if (top2 == -1)
        return -1;
    return pop2();
}

int peek()
{
    transfer();
    if (top2 == -1)
        return -1;
    return s2[top2];
}

int main()
{
    int choice, x;

    while(1)
    {
        printf("1.Enqueue  2.Dequeue  3.Peek  4.Exit\n");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                printf("Enter element: ");
                scanf("%d", &x);
                enqueue(x);
                break;

            case 2:
                x = dequeue();
                if(x != -1)
                    printf("Deleted: %d\n", x);
                break;

            case 3:
                x = peek();
                if(x != -1)
                    printf("Front: %d\n", x);
                break;

            case 4:
                return 0;

            default:
                printf("Invalid choice\n");
        }
    }
}