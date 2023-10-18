package test;
import java.util.*;
public class test {
    public static void main(String[] args) {
        String today = "17";
//        String terms = "271";
//        String[] goal = {"2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"};
        test t = new test();
//        for(int x : t.solution(today,terms)){
//            System.out.println(x);
//        }
        System.out.println(t.solution(today));


    }

    boolean check[] = new boolean[7];
    List<String> list = new ArrayList<>();
    public int solution(String numbers) {
        int answer = 0;

        for(int i=0; i<numbers.length(); i++){
            DFS(i+1, numbers, "");
        }
        for(int i=0; i<list.size(); i++) {
            System.out.println(list.get(i));
        }

        for(int i=0; i<list.size(); i++){
            if(prime(Integer.parseInt(list.get(i)))) answer++;
        }

        return answer;
    }
    public void DFS(int L, String numbers, String tmp){
        if(tmp.length() == L){
            if(!list.contains(tmp)) list.add(tmp);
            return;
        }

        for(int i=0; i<numbers.length(); i++){
            if(!check[i]){
                tmp += numbers.charAt(i);
                check[i] = true;
                DFS(L, numbers, tmp);
                check[i] = false;
                tmp = tmp.substring(0, tmp.length()-1);
            }
        }
        return;
    }
    public boolean prime(int n){
        if(n == 0 || n == 1) return false;
        for(int i=2; i<n; i++){
            if(n%i==0) return false;
        }
        return true;
    }

}