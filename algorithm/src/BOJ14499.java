import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ14499 {
    static int n, m, x, y;
    static int[][] map;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {1, -1, 0, 0};
    static int[] dice = {0, 0, 0, 0, 0, 0, 0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        map = new int[n][m];
        for(int i = 0; i <n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < m; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < k; i++){
            move(Integer.parseInt(st.nextToken()));
        }

    }

    public static void move(int dir){
        int nx = x + dx[dir-1];
        int ny = y + dy[dir-1];
        if(nx >= 0 && nx < n && ny >= 0 && ny < m){
            stamp(dir, nx, ny);
            x = nx;
            y = ny;
            System.out.println(dice[1]);
        }
    }

    public static void stamp(int dir, int x, int y){
        int tmp = dice[1];
        switch (dir) {
            case 1:
                dice[1] = dice[4];
                dice[4] = dice[6];
                dice[6] = dice[3];
                dice[3] = tmp;
                break;
            case 2:
                dice[1] = dice[3];
                dice[3] = dice[6];
                dice[6] = dice[4];
                dice[4] = tmp;
                break;
            case 3:
                dice[1] = dice[5];
                dice[5] = dice[6];
                dice[6] = dice[2];
                dice[2] = tmp;
                break;
            case 4:
                dice[1] = dice[2];
                dice[2] = dice[6];
                dice[6] = dice[5];
                dice[5] = tmp;
                break;
        }
        if (map[x][y] == 0) {
            map[x][y] = dice[6];
        }
        else{
            dice[6] = map[x][y];
            map[x][y] = 0;
        }
    }

}
