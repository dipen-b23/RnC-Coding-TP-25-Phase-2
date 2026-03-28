#include <stdio.h>

#define MAX 100

char stack[MAX];
int top = -1;

void push(char ch)
{
    stack[++top] = ch;
}

char pop()
{
    if(top==-1)
        return '\0';
    return stack[top--];
}

int isMatching(char open, char close)
{
    if(open == '(' && close == ')') return 1;
    if(open == '{' && close == '}') return 1;
    if(open == '[' && close == ']') return 1;
    return 0;
}

int isBalanced(char brac[])
{
    for(int i = 0; brac[i]!='\0'; i++)
    {
        char ch = brac[i];
        if(ch == '(' || ch == '{' || ch == '[')
            push(ch);
        else if(ch == ')' || ch == '}' || ch == ']')
        {
            char p = pop();
            if (!isMatching(p,ch))
                return 0;
        }
    }
    if(top==-1)
            return 1;
        else
            return 0;
}

int main()
{
    char brac[100];
    printf("Enter expression: ");
    scanf("%s", brac);

    if (isBalanced(brac))
        printf("Balanced");
    else
        printf("Not Balanced");

    return 0;
}
