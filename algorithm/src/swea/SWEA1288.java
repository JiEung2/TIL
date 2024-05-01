package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SWEA1288 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 0; tc < T; tc++) {
            int n = Integer.parseInt(br.readLine());
            System.out.println("#" + (tc+1) +" "+ solve(n));
        }
    }

    public static int solve(int n) {
        int cnt = 1;
        int target = (1 << 10) - 1;
        int now = 0;
        while (true) {
            String number = Integer.toString(n * cnt);
            for (int i = 0; i < number.length(); i++) {
                int tmpN = number.charAt(i) - '0';
                now = now | (1 << tmpN);
                if (now == target) return n * cnt;
            }
            cnt++;
        }
    }
}
