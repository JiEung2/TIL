package stringCharacter;

import java.io.*;

public class WordInSentence {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] arr = br.readLine().split(" ");
        int max = 0;
        for(int i=1; i< arr.length; i++){
            if(arr[max].length() < arr[i].length()){
                max = i;
            }
        }
        System.out.println(arr[max]);
    }
}
