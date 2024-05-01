package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ13458 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        long result = 0;

        for(int i = 0; i < n; i++){
            arr[i] -= b;
            result++;

            if(arr[i] > 0) {
                if (arr[i] >= c) {
                    result += arr[i] / c;
                    if (arr[i] % c != 0){
                        result++;
                    }
                } else {
                    result++;
                }
            }
        }

        System.out.println(result);

    }
}
