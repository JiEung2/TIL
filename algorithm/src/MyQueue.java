public class MyQueue {
    class Node {

    }

    Node front, rear;

    public MyQueue() {
        front = null;
        rear = null;
    }

    Node newNode;

    public void enQueue(String data) {
        if (isEmpty()) {
            newNode = addElement(data);
        }

        front = newNode;
        rear = newNode;
    }
    else

    {
        newNode = addElement(data);
        rear = newNode;
    }

    public String deQueue() {
        if (isEmpty()) {
            System.out.println("Queue is Empty");
            return null;
        }
    }

    String data = front.getData();
    front =front.next;
    if(front ==null){
        rear = null;
    }

    return data;
}
