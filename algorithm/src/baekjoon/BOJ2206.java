package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ2206 {
    static int n, m;
    static int result = Integer.MAX_VALUE;
    static int[][] arr;
    static int[][][] visited;

    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static int[][] check;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n][m];
        visited = new int[n][m][2];
        for(int[][] v : visited){
            for(int[] vv : v){
                Arrays.fill(vv, n*m +1);
            }
        }

        for(int i = 0; i < n; i++){
            String tmp = br.readLine();
            char[] c = tmp.toCharArray();
            for(int j = 0; j < m; j++){
                arr[i][j] = c[j] - '0';
            }
        }
        check = new int[n][m];
        bfs(0, 0);
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                System.out.print(visited[i][j][0] + " ");
            }
            System.out.println();
        }
        System.out.println();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                System.out.print(visited[i][j][1] + " ");
            }
            System.out.println();
        }
        if(visited[n-1][m-1][0] == n*m+1 && visited[n-1][m-1][1] == n*m+1) System.out.println(-1);
        else System.out.println(Math.min(visited[n-1][m-1][0], visited[n-1][m-1][1]));
    }

    public static void bfs(int x, int y){
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{x,y});
        visited[x][y][0] = 1;

        while(!q.isEmpty()){
            int[] point = q.poll();
            int tx = point[0];
            int ty = point[1];
            for(int i = 0; i < 4; i++){
                int nx = tx + dx[i];
                int ny = ty + dy[i];
                if(nx >= 0 && nx < n && ny >= 0 && ny < m){
                    int c = check[tx][ty];
                    if (arr[nx][ny] == 0){
                        if(visited[nx][ny][c] > visited[tx][ty][c] + 1){
                            visited[nx][ny][c] = visited[tx][ty][c] + 1;
                            check[nx][ny] = check[tx][ty];
                            q.add(new int[]{nx,ny});
                        }
                    }
                    else{
                        if(c == 1) continue;
                        if(visited[nx][ny][1] > visited[tx][ty][0] + 1){
                            visited[nx][ny][1] = visited[tx][ty][0] + 1;
                            check[nx][ny] = 1;
                            q.add(new int[]{nx,ny});
                        }
                    }
                }
            }
        }

    }
}
