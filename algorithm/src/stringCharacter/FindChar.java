package stringCharacter;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class FindChar {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String tmp = br.readLine();
        char ch = br.readLine().charAt(0);
        tmp = tmp.toLowerCase();
        char[] arr = tmp.toCharArray();
        ch = Character.toLowerCase(ch);
        int cnt=0;
        for(int i=0; i<arr.length; i++){
            if(arr[i] == ch) cnt++;
        }
        System.out.println(cnt);
    }
}