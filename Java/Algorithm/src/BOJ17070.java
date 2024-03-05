import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ17070 {
    static int n;
    static int[][] arr;
    static int state;
    static int[] dx = {0, 1, 1};
    static int[] dy = {1, 1, 0};
    static int cnt;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n][n];

        for(int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        state = 0;

        move(0, 1);
        System.out.println(cnt);

    }

    public static void move(int x, int y) {
        if(x == n-1 && y == n-1) {
            cnt++;
            return;
        }
        if(state == 0) {
            moveHor(x, y);
            state = 1;
            moveCross(x, y);
            state = 0;
        }
        else if(state == 1){
            state = 0;
            moveHor(x, y);
            state = 1;
            moveCross(x, y);
            state = 2;
            moveVer(x, y);
            state = 1;
        }
        else {
            moveVer(x, y);
            state = 1;
            moveCross(x, y);
            state = 2;
        }
    }

    public static void moveHor(int x, int y) {
        int nx = x + dx[0];
        int ny = y + dy[0];
        if(nx >= 0 && nx < n && ny >= 0 && ny < n && arr[nx][ny]==0) {
            move(nx, ny);
        }
    }

    public static void moveVer(int x, int y) {
        int nx = x + dx[2];
        int ny = y + dy[2];
        if(nx >= 0 && nx < n && ny >= 0 && ny < n && arr[nx][ny]==0) {
            move(nx, ny);
        }
    }

    public static void moveCross(int x, int y) {
        boolean flag = true;
        for(int i = 0; i < 3; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(!(nx >= 0 && nx < n && ny >= 0 && ny < n && arr[nx][ny]==0)) {
                flag = false;
                break;
            }
        }
        if(flag) {
            move(x + dx[1], y + dy[1]);
        }
    }

}
