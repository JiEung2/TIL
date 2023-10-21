package test;
import java.util.*;
public class test {
    public static void main(String[] args) {
        test t= new test();
        String babbling[] = {"ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"};
        System.out.println(t.solution(babbling));


    }

    List<String> list = new ArrayList<>();
    boolean[] check = new boolean[4];
    public int solution(String[] babbling) {
        int answer = 0;

        String[] words = {"aya", "ye", "woo", "ma"};
        for(int i=0; i<words.length; i++){
            check[i] = true;
            DFS(words[i], words);
            check[i] = false;
        }
        for(String word : babbling){
            if(list.contains(word)) answer++;
        }
        return answer;
    }

    public void DFS(String word, String[] words){
        System.out.println(word);
        list.add(word);
        for(int i=0; i<words.length; i++){
            if(check[i]) continue;
            check[i] = true;
            DFS(word+words[i], words);
            check[i] = false;
            if (word.length() >= words[i].length()) {
                word = word.substring(0, word.length() - words[i].length());
            }
        }
    }


}