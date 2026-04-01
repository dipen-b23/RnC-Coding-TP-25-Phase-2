#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


struct Node {
    int data;
    struct Node* next;
};


bool detectLoop(struct Node* head) {
    struct Node *slow = head, *fast = head;

    while (slow && fast && fast->next) {
        slow = slow->next;          
        fast = fast->next->next;    

        
        if (slow == fast) {
            return true;
        }
    }
    
    return false;
}


struct Node* newNode(int data) {
    struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
    temp->data = data;
    temp->next = NULL;
    return temp;
}

int main() {
    
    struct Node* head = newNode(10);
    head->next = newNode(20);
    head->next->next = newNode(30);
    head->next->next->next = newNode(40);

    
    head->next->next->next->next = head->next;

    if (detectLoop(head))
        printf("Loop is detected\n");
    else
        printf(" Loop is not detected.\n");

    return 0;
    
}
