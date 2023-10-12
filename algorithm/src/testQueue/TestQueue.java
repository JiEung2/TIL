package testQueue;

import testQueue.CustomQueue;

public class TestQueue {
    public static void main(String[] args) {
        CustomQueue q = new CustomQueue();
        for(int i=1; i<=10; i++){
            q.inQueue(i);
        }

        for(int i=0; i<10; i++){
            System.out.println(q.deQueue());
        }
    }

}
