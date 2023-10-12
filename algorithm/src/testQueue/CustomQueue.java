package testQueue;

import java.util.Stack;

public class CustomQueue {
    private Stack<Integer> A = new Stack<>();
    private Stack<Integer> B = new Stack<>();
    public void inQueue(int n){
        A.push(n);
    }

    public int deQueue(){
        if(A.isEmpty()){
            return B.pop();
        }
        while(!A.isEmpty()){
            int tmp = A.pop();
            B.push(tmp);
        }
        return B.pop();
    }
}
