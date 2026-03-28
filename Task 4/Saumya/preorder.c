#include <stdio.h>
#include <stdlib.h>

struct Node{
    int data;
    struct Node* left;
    struct Node* right;
};

struct Node* newNode(int x)
{
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = x;
    node->left = NULL;
    node->right = NULL;
    return node;
}

void preOrder(struct Node* node)
{
    if (node == NULL)
        return;

        printf("%d ", node->data);
        preOrder(node->left);
        preOrder(node->right);
}

int main()
{
    struct Node* root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
    root->right->left = newNode(6);
    root->right->right = newNode(7);
    preOrder(root);
    return 0;

    /* 
                1
        2               3
    4       5       6       7

    1 2 4 5 3 6 7
    */
}
