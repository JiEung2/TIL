package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ16236 {
    static class Point{
        int x, y;
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int n, x, y, result;
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int[][] dis;
    static int[][] map;
    static int size = 2;
    static int nowEating = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        map = new int[n][n];
        result = 0;
        for(int i = 0; i < n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 9) {
                    x = i;
                    y = j;
                }
            }
        }

        while (true) {
            checkDistance();
            if (selectFish()) {
                break;
            }
        }
        System.out.println(result);

    }

    public static void checkDistance() {
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(x, y));
        dis = new int[n][n];
        dis[x][y] = 1;
        while (!q.isEmpty()) {
            Point p = q.poll();
            for(int i = 0; i < 4; i++){
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n && dis[nx][ny] == 0 && map[nx][ny] <= size) {
                    dis[nx][ny] = dis[p.x][p.y] + 1;
                    q.add(new Point(nx, ny));
                }
            }
        }
    }

    public static boolean selectFish() {
        int minD = Integer.MAX_VALUE;
        int minX = -1;
        int minY = -1;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if (size > map[i][j] && map[i][j] > 0 && dis[i][j] != 0) {
                    if (dis[i][j] < minD) {
                        minD = dis[i][j];
                        minX = i;
                        minY = j;
                    }
                }
            }
        }
        if (minX != -1) {
            map[x][y] = 0;
            result += dis[minX][minY] - 1;
            x = minX;
            y = minY;
            map[x][y] = 0;
            nowEating++;
            if (nowEating == size) {
                size++;
                nowEating = 0;
            }
            return false;
        }
        return true;
    }
}
