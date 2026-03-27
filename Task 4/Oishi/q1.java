class MyStack {
    char [] arr;
    int top;
    int cap;

    MyStack(int cap) {
        this.cap = cap;
        arr = new char[cap];
        top = -1;
    }

    void push( char x) {
        if (top == cap - 1) {
            System.out.println("Stack Overflow");
            return;
        }
        arr[++top] = x;
    }

    char pop() {
        if (top == -1) {
            System.out.println("Stack Underflow");
            return '/';
        }
        return arr[top--];
    }


    boolean isEmpty() {
        return top == -1;
    }
}

public class q1{
    static boolean balanced (String str) {
        MyStack stack = new MyStack(str.length());

        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);

            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            }

            else {
                if (stack.isEmpty()) {
                    return false;
                }

                char top = stack.pop();

                if ((ch == ')' && top != '(') ||
                    (ch == '}' && top != '{') ||
                    (ch == ']' && top != '[')) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }

    public static void main(String[] args) {
        String s1 = "{[()]}";
        String s2 = "{[(])}";

        if (balanced (s1)){
            System.err.println("S1 is Balanced");
        }
        else {
            System.out.println("S1 is not balanced");
        }

        if (balanced (s2)){
            System.err.println("S2 is Balanced");
        }
        else {
            System.out.println("S2 is not balanced");
        }  
    }
}
