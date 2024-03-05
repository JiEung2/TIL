import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ14888 {
    static int opNum, n;
    static int[] op = new int[4];
    static int[] arr, oper;
    static int max = Integer.MIN_VALUE;
    static int min = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        arr = new int[n];

        for(int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }


        st = new StringTokenizer(br.readLine());
        opNum = n-1;
        for(int i = 0; i < 4; i++) {
            op[i] = Integer.parseInt(st.nextToken());
        }
        oper = new int[opNum];
        DFS(0);

        System.out.println(max);
        System.out.println(min);
    }

    public static void DFS(int L) {
        if(L == opNum) {
            check();
            return;
        }

        for(int i = 0; i < 4; i++) {
            if(op[i] > 0) {
                op[i] -= 1;
                oper[L] = i;
                DFS(L + 1);
                op[i] += 1;
            }
        }
    }

    public static void check() {
        int num = arr[0];
        for(int i = 1; i < n; i++) {
            num = calc(num, arr[i], oper[i-1]);
        }
        max = Math.max(max, num);
        min = Math.min(min, num);
    }

    public static int calc(int num1, int num2, int op) {
        if(op == 0) return num1 + num2;
        if(op == 1) return num1 - num2;
        if(op == 2) return num1 * num2;
        if(num1 < 0) {
            return -(-num1 / num2);
        }
        return num1 / num2;
    }
}
