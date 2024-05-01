package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ14503 {
    static int[][] map;
    static int n, m, cnt;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        map = new int[n][m];
        cnt = 0;
        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < m; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        solve(x, y, d);
        System.out.println(cnt);
    }

    public static void solve(int x, int y, int d){
        if (map[x][y] == 0) {
            cnt++;
            map[x][y] = 2;
        }

        for(int i = 0; i < 4; i++){
            d = (d + 3) % 4;
            int nx = x + dx[d];
            int ny = y + dy[d];
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && map[nx][ny] == 0){
                solve(nx, ny, d);
                return;
            }
        }

        int tmp = (d + 2) % 4;

        int nx = x + dx[tmp];
        int ny = y + dy[tmp];
        if (nx >= 0 && nx < n && ny >= 0 && ny < m && map[nx][ny] != 1){
            solve(nx, ny, d);
        }

    }

}