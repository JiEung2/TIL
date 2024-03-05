import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class BOJ9935 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		String bomb = br.readLine();
		
		Stack<Character> stack = new Stack<>();
		char[] chars = str.toCharArray();
		for(char x : chars) {
			stack.add(x);
			if(stack.size() >= bomb.length()) {
				boolean flag = true;
				for(int i = 0; i < bomb.length(); i++) {
					if(stack.get(stack.size() - bomb.length() + i) != bomb.charAt(i)) {
						flag = false;
						break;
					}
				}
				if(flag) {
					for(int i = 0; i < bomb.length(); i++) {
						stack.pop();
					}
				}
			}
			
		}
		StringBuilder sb = new StringBuilder();
		if(stack.isEmpty()) {
			System.out.println("FRULA");
		}
		else {
			for(Character c : stack) {
				sb.append(c);
			}
			System.out.println(sb.toString());
		}
	}

}
