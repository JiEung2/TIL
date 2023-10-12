package stringCharacter;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class PalindromeString {
    public static void main(String[] args) throws IOException {
        PalindromeString t = new PalindromeString();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();
        word = word.toLowerCase();
        System.out.println(t.solution(word));

    }
    public String solution(String word){
        int lp = 0, rp = word.length()-1;
        while(lp<rp){
            if(word.charAt(lp)==word.charAt(rp)){
                lp++;
                rp--;
            }
            else return "NO";
        }
        return "YES";
    }
}
