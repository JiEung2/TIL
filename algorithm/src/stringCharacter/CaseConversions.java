package stringCharacter;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class CaseConversions {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String tmp = br.readLine();
        char[] ch = tmp.toCharArray();
        for(char c : ch){
            if(Character.isUpperCase(c)) System.out.print(Character.toLowerCase(c));
            else System.out.print(Character.toUpperCase(c));
        }
    }
}
