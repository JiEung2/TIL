import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ2573 {
    static boolean checkIsland;
    static int n;
    static int m;
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int[][] visited;
    static int[][] map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        map = new int[n][m];


        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int cnt = 0;
        int[][] tmp;
        while (true) {
            visited = new int[n][m];
            tmp = new int[n][m];
            checkIsland = false;
            cnt++;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (map[i][j] > 0) {
                        for (int d = 0; d < 4; d++) {
                            int nx = i + dx[d];
                            int ny = j + dy[d];
                            if (nx >= 0 && nx < n && ny >= 0 && ny < m && map[nx][ny] == 0) {
                                tmp[i][j]++;
                            }
                        }
                    }
                }
            }
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    map[i][j] -= tmp[i][j];
                    if (map[i][j] < 0){
                        map[i][j] = 0;
                    }
                }
            }
            boolean flag = true;
            boolean flag2 = true;
            int x = 0;
            int y = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (map[i][j] != 0) {
                        x = i;
                        y = j;
                        flag2 = false;
                        break;
                    }
                }
                if(!flag2) {
                    break;
                }
            }
            visited[x][y] = 1;
            check(x, y);
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (map[i][j] > 0 && visited[i][j] == 0) {
                        checkIsland = true;
                        break;
                    }
                }
                if(checkIsland) break;
            }
            if (checkIsland) {
                break;
            } else {
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < m; j++) {
                        if (map[i][j] != 0) {
                            flag = false;
                            break;
                        }
                    }
                    if(!flag) {
                        break;
                    }
                }
                if (flag) {
                    cnt = 0;
                    break;
                }
            }
        }
        System.out.println(cnt);
    }

    public static void check(int sx, int sy) {
        for (int i = 0; i < 4; i++) {
            int nx = sx + dx[i];
            int ny = sy + dy[i];
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && map[nx][ny] > 0 && visited[nx][ny] == 0) {
                visited[nx][ny] = 1;
                check(nx, ny);
            }
        }
    }
}