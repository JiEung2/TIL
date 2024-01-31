package test;
import java.util.*;
public class test5 {
    public static void main(String[] args) {
        String s = "[](){}";
        System.out.println(solution(s));
    }
    public static int solution(String s) {
        int answer = 0;
        for(int i = 0; i < s.length() + 1; i++){
            s = s.substring(1, s.length()) + s.substring(0, 1);
            answer += check(s);
        }
        return answer;
    }

    public static int check(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (!stack.isEmpty()) {
                char tmp = stack.peek();
                if ((tmp == '[' && c == ']') || (tmp == '(' && c == ')') || (tmp == '{' && c == '}')) {
                    stack.pop();
                } else
                    stack.add(c);
            } else
                stack.add(c);
        }
        if(stack.isEmpty())
            return 1;
        return 0;
    }
}
