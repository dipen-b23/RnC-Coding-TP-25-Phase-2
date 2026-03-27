class MyStack {
    int[] arr;
    int top;
    int capacity;

    MyStack(int cap) {
        capacity = cap;
        arr = new int[cap];
        top = -1;
    }

    void push(int x) {
        if (top == capacity - 1) {
            System.out.println("Stack Overflow");
            return;
        }
        arr[++top] = x;
    }

    int pop() {
        if (top == -1) {
            System.out.println("Stack Underflow");
            return -1;
        }
        return arr[top--];
    }

    int peek() {
        if (top == -1) {
            return -1;}
        return arr[top];
    }

    boolean isEmpty() {
        return top == -1;
    }
}

class queue {
    MyStack s1;
    MyStack s2;

    queue(int cap) {
        s1 = new MyStack(cap);
        s2 = new MyStack(cap);
    }

    void enqueue(int x) {
        s1.push(x);
    }

    int dequeue() {
        if (s1.isEmpty() && s2.isEmpty()) {
            System.out.println("Queue is empty");
            return -1;
        }

        if (s2.isEmpty()) {
            while (!s1.isEmpty()) {
                s2.push(s1.pop());
            }
        }

        return s2.pop();
    }

    int peek() {
        if (s1.isEmpty() && s2.isEmpty()) {
            System.out.println("Queue is empty");
            return -1;
        }

        if (s2.isEmpty()) {
            while (!s1.isEmpty()) {
                s2.push(s1.pop());
            }
        }
        return s2.peek();
    }
}

public class q3 {
    public static void main(String[] args) {
        queue q = new queue(5);

        q.enqueue(1);
        q.enqueue(2);
        q.enqueue(3);
        q.enqueue(4);

        System.out.println(q.dequeue()); 
        System.out.println(q.peek());   
    }
}



