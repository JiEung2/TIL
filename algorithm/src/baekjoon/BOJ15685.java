package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ15685 {
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, -1, 0, 1};
    static int result = 0;
    static int[][] map = new int[101][101];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int g = Integer.parseInt(st.nextToken());
            checkCurve(x, y, d, g);
        }
        count();
        System.out.println(result);
    }

    public static void checkCurve(int x, int y, int d, int g) {
        List<Integer> dir = new ArrayList<>();
        dir.add(d);
        for(int i = 0 ; i<g; i++){
            for(int j = dir.size()-1; j >= 0 ; j--){
                dir.add((dir.get(j) + 1) % 4);
            }
        }
        draw(x, y, dir);
    }

    public static void draw(int x, int y, List<Integer> dir){
        map[x][y] = 1;
        int tx = x;
        int ty = y;
        for(int i = 0; i < dir.size(); i++){
            int d = dir.get(i);
            int nx = tx + dx[d];
            int ny = ty + dy[d];
            map[nx][ny] = 1;
            tx += dx[d];
            ty += dy[d];
        }
    }

    public static void count() {
        for(int i = 0; i < 100; i++){
            for(int j = 0; j < 100; j++){
                if (map[i][j] == 1 && map[i + 1][j] == 1 && map[i][j + 1] == 1 && map[i + 1][j + 1] == 1) {
                    result++;
                }
            }
        }
    }

}
