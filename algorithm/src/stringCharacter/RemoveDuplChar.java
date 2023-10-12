package stringCharacter;

import java.io.*;
import java.util.HashMap;

public class RemoveDuplChar {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String tmp = br.readLine();
        for(int i=0; i<tmp.length(); i++){
            if(tmp.indexOf(tmp.charAt(i))==i){
                System.out.print(tmp.charAt(i));
            }
        }

    }
}
