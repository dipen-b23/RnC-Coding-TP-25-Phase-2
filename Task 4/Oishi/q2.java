class node {
    int data;
    node next;
    node (int data){
        this.data = data;
        this.next = null;
    }
}

public class q2{
    static boolean check (node head){
        node slow = head;
        node fast = head;

        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast){
                return true;
            }          
        }        
        return false;
    }

    public static void main (String [] args){
        node head = new node (1);
        head.next = new node (2);
        head.next.next = new node (3);
        head.next.next.next = new node (4);
        head.next.next.next.next = new node (5);

        head.next.next.next.next = head.next.next;
        if (check(head)){
            System.out.println("Yes");
        }
        else {
            System.out.println("No");
        }
    }
}
