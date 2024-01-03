package test;

import java.util.Stack;

public class test3 {
    public int solution(String s)
    {
        int answer = -1;
        Stack<Character> stack = new Stack();
        for(int i=0; i<s.length(); i++){
            if (!stack.isEmpty() && stack.peek() == s.charAt(i)) {
                stack.pop();
            }
            else stack.push(s.charAt(i));
        }

        return answer;
    }
}
