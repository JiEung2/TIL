package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ17140 {
    static class Number implements Comparable<Number>{
        int num;
        int cnt;

        public Number(int num, int cnt) {
            this.num = num;
            this.cnt = cnt;
        }

        @Override
        public int compareTo(Number o) {
            if (this.cnt == o.cnt) return this.num - o.num;
            return this.cnt - o.cnt;
        }
    }
    static int r, c, k, rLength, cLength;
    static int[][] arr = new int[100][100];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        rLength = 3;
        cLength = 3;

        for(int i = 0; i < 3; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < 3; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        System.out.println(solve());
    }
    public static void p(){
        for(int i = 0 ; i < cLength ; i++){
            for(int j = 0; j < rLength; j++){
                System.out.print(arr[i][j]);
            }
            System.out.println();
        }
        System.out.println();
    }
    public static int solve(){
        for(int i = 0; i <= 100; i++){
            if(arr[r-1][c-1] == k) return i;
            selectCal();
//            p();
        }
        return -1;
    }

    public static void selectCal() {
        if (rLength <= cLength){
            rCal();
        }
        else cCal();
    }

    public static void rCal(){
        PriorityQueue<Number> pq = new PriorityQueue<>();
        int tmpLength = 0;

        for(int i = 0; i < cLength; i++){
            Map<Integer, Integer> map = new HashMap<>();
            for(int j = 0; j < rLength; j++){
                if(arr[i][j] == 0) continue;
                map.put(arr[i][j], map.getOrDefault(arr[i][j], 0)+1);
            }
//            map.forEach((k, v) -> System.out.println("key = " + k + "  value = " + v));
//            System.out.println();
            map.forEach((k, v) -> pq.add(new Number(k, v)));

            int index = 0;
            while (!pq.isEmpty() && index < 100) {
                Number N = pq.poll();
                arr[i][index] = N.num;
                arr[i][index+1] = N.cnt;
                index += 2;
            }
            tmpLength = Math.max(tmpLength, index);

            for (;index < 100; index++){
                arr[i][index] = 0;
            }
        }

        rLength = tmpLength;
    }

    public static void cCal(){
        PriorityQueue<Number> pq = new PriorityQueue<>();
        int tmpLength = 0;

        for(int i = 0; i < rLength; i++){
            Map<Integer, Integer> map = new HashMap<>();
            for(int j = 0; j < cLength; j++){
                if(arr[j][i] == 0) continue;
                map.put(arr[j][i], map.getOrDefault(arr[j][i], 0)+1);
            }
//            map.forEach((k, v) -> System.out.println("key = " + k + "  value = " + v));
//            System.out.println();
            map.forEach((k, v) -> pq.add(new Number(k, v)));

            int index = 0;
            while (!pq.isEmpty() && index < 100) {
                Number N = pq.poll();
                arr[index][i] = N.num;
                arr[index+1][i] = N.cnt;
                index += 2;
            }
            tmpLength = Math.max(tmpLength, index);

            for (;index < 100; index++){
                arr[index][i] = 0;
            }
        }

        cLength = tmpLength;
    }
}
