import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ14500 {
    static int n, m;
    static int[][] map;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int result = 0;
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        map = new int[n][m];
        visited = new boolean[n][m];

        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < m; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                visited[i][j] = true;
                tetro(i, j, map[i][j], 1);
                visited[i][j] = false;
            }
        }
        System.out.println(result);
    }

    public static void tetro(int x, int y, int sum, int L){
        if (L == 4) {
            result = Math.max(result, sum);
            return;
        }

        for(int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                continue;
            }

            if (!visited[nx][ny]) {
                if (L == 2) {
                    visited[nx][ny] = true;
                    tetro(x, y, sum + map[nx][ny], L + 1);
                    visited[nx][ny] = false;
                }
                visited[nx][ny] = true;
                tetro(nx, ny, sum + map[nx][ny], L + 1);
                visited[nx][ny] = false;
            }
        }
    }
}
