import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ14891 {
    static int k;
    static int[][] cogwheel;
    static int[] check_dir;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        cogwheel = new int[4][8];
        for (int i = 0; i < 4; i++) {
            String tmp = br.readLine();
            for(int j = 0; j < 8; j++){
                cogwheel[i][j] = tmp.charAt(j) - '0';
            }
        }
        k = Integer.parseInt(br.readLine());
        for (int i = 0; i < k; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int target = Integer.parseInt(st.nextToken());
            int dir = Integer.parseInt(st.nextToken());
            check_dir = new int[4];
            check(target-1, dir);
            rotate();
        }
        int result = 0;
        if (cogwheel[0][0] == 1) result += 1;
        if (cogwheel[1][0] == 1) result += 2;
        if (cogwheel[2][0] == 1) result += 4;
        if (cogwheel[3][0] == 1) result += 8;

        System.out.println(result);
    }
    public static void check(int target, int dir){
        check_dir[target] = dir;
        for(int i = target - 1; i >= 0; i--){
            if(cogwheel[i][2] != cogwheel[i+1][6]) check_dir[i] = -check_dir[i+1];
            else break;
        }
        for(int i = target + 1; i < 4; i++){
            if(cogwheel[i][6] != cogwheel[i-1][2]) check_dir[i] = -check_dir[i-1];
            else break;
        }
    }
    public static void rotate() {
        for(int i = 0; i < 4; i++){
            if(check_dir[i] == 1){
                int tmp = cogwheel[i][7];
                for(int j = 7; j > 0; j--){
                    cogwheel[i][j] = cogwheel[i][j-1];
                }
                cogwheel[i][0] = tmp;
            }
            if(check_dir[i] == -1){
                int tmp = cogwheel[i][0];
                for(int j = 0; j < 7; j++){
                    cogwheel[i][j] = cogwheel[i][j+1];
                }
                cogwheel[i][7] = tmp;
            }
        }
    }
}
