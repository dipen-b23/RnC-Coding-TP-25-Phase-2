#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int data;
    struct Node* next;
} Node;

Node* createNode(int data)
{
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

int detectLoop(Node* head)
{
    Node* slow = head;
    Node* fast = head;

    while(fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;

        if(slow == fast)
            return 1;
    }
    return 0;
}

int main()
{
    int n, x, pos;
    printf("Enter number of nodes: ");
    scanf("%d", &n);

    Node *head = NULL, *temp = NULL, *loopNode = NULL;

    for(int i = 1; i <= n; i++)
    {
        scanf("%d", &x);
        Node* newNode = createNode(x);

        if(head == NULL)
        {
            head = newNode;
            temp = newNode;
        }
        else
        {
            temp->next = newNode;
            temp = newNode;
        }
    }

    printf("Enter position to create loop (0 for no loop): ");
    scanf("%d", &pos);

    if(pos > 0 && pos <= n)
    {
        loopNode = head;
        for(int i = 1; i < pos; i++)
            loopNode = loopNode->next;

        temp->next = loopNode;
    }

    if(detectLoop(head))
        printf("Yes");
    else
        printf("No");

    return 0;
}