package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SWEA3234 {
    static int cnt;
    static int n;
    static int[] weight;
    static int[] check;
    static int[] per_check;
    static int[] tmp;
    static int sum;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int tc = 0; tc < T; tc++) {
            cnt = 0;
            n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            weight = new int[n];
            check = new int[n];
            per_check = new int[n];
            tmp = new int[n];
            sum = 0;
            for(int i = 0; i<n; i++) {
                weight[i] = Integer.parseInt(st.nextToken());
                sum += weight[i];
            }
            per(0);
            System.out.println("#" + (tc+1)+ " " + cnt);
        }
    }

    public static void dfs(int sumLeft, int sumRight) {
        if(sumLeft < sumRight) return;
        else {
            for(int i = 0; i < n; i++){
                if(check[i] == 0)
                    System.out.print(tmp[i]);
            }
            System.out.println();
            for(int i = 0; i < n; i++){
                if(check[i] == 1)
                    System.out.print(tmp[i]);
            }
            System.out.println();
            cnt++;
        }

        for(int i = 0; i<n; i++) {
            if(check[i] == 0) {
                check[i] = 1;
                dfs(sumLeft - tmp[i], sumRight + tmp[i]);
                check[i] = 0;
            }
        }
    }

    public static void per(int L){
        if(L == 3){
            dfs(sum, 0);
            for(int i = 0; i < n ; i++){
                System.out.print(tmp[i]);
            }
            System.out.println();
            return;
        }

        for(int i = 0 ; i < n; i++){
            if (per_check[i] == 0) {
                per_check[i] = 1;
                tmp[L] = weight[i];
                per(L + 1);
                per_check[i] = 0;
            }
        }
    }
}