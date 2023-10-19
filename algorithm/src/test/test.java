package test;
import java.util.*;
public class test {
    public static void main(String[] args) {
        test t= new test();
        int k = 80;
        int[][] dungeons = {{80,20},{50,40},{30,10}};
        System.out.println(t.solution(k, dungeons));


    }

    class Solution {
        int[][] arr;
        public int solution(int n, int[][] wires) {
            int answer = n;
            arr = new int[n+1][n+1];


            for(int i=0; i<wires.length; i++){
                arr[wires[i][0]][wires[i][1]] = 1;
                arr[wires[i][1]][wires[i][0]] = 1;
            }

            int n1 = 0, n2 = 0;

            for(int i=0; i<wires.length; i++){
                n1 = wires[i][0];
                n2 = wires[i][1];

                arr[n1][n2] = 0;
                arr[n2][n1] = 0;

                answer = Math.min(answer, BFS(n, n1));

                arr[n1][n2] = 1;
                arr[n2][n1] = 1;
            }

            return answer;
        }

        public int BFS(int n, int n1){
            int cnt = 1;
            boolean[] check = new boolean[n+1];

            Queue<Integer> queue = new LinkedList<>();
            queue.add(n1);

            while(!queue.isEmpty()){
                int point= queue.poll();
                check[point] = true;

                for(int i=1; i<n+1; i++){
                    if(check[i]) continue;
                    if(arr[point][i]==1) {
                        queue.add(i);
                        cnt++;
                    }
                }
            }
            return (int)Math.abs(n-2*cnt);
        }
    }


}