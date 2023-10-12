package stringCharacter;

import java.io.*;

public class FlipSpecificChar {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] arr = br.readLine().toCharArray();
        int lp = 0, rp = arr.length-1;
        while(lp<rp){
            if(!Character.isAlphabetic(arr[lp])) lp++;
            else if(!Character.isAlphabetic(arr[rp])) rp--;
            else{
                char tmp = arr[lp];
                arr[lp] = arr[rp];
                arr[rp] = tmp;
                lp++;
                rp--;
            }
        }
        for(char x : arr) System.out.print(x);
    }
}
