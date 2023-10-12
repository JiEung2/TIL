package stringCharacter;

import java.io.*;
public class FlipWords {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for(int i=0; i<n; i++){
            String tmp = br.readLine();
            for(int j=tmp.length()-1; j>=0; j--){
                System.out.print(tmp.charAt(j));
            }
            System.out.println();
        }
    }
}
