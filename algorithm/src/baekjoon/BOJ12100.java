package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ12100 {
    static int[][] board;
    static int n, max = 0;
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int[] c;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        board = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        c = new int[5];
        DFS(0);
        System.out.println(max);
    }

    public static void DFS(int L) {
        if (L == 5) {
            int[][] newBoard = deepCopy(board);
            for(int i = 0; i < 5; i++){
                newBoard = move(newBoard, c[i]);
//                for(int z = 0; z < n; z++){
//                    for(int j = 0; j < n; j++){
//                        System.out.print(newBoard[z][j]);
//                    }
//                    System.out.println();
//                }
//                System.out.println();
            }
            max = Math.max(max, calcMax(newBoard));
            return;
        }

        for(int i = 0 ; i < 4; i++){
            c[L] = i;
            DFS(L+1);
        }
    }
    public static int[][] deepCopy(int[][] original) {
        int[][] result = new int[n][n];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                result[i][j] = original[i][j];
            }
        }
        return result;
    }
    public static int[][] move(int[][] arr, int d) {
        boolean[][] flag = new boolean[n][n];
        if(d < 2){
            for (int i = n-1; i >= 0; i--) {
                for (int j = n-1; j >= 0; j--) {

                    int number = 0;
                    int nx = 0;
                    int ny = 0;
                    if(d == 0){
                        if(arr[j][i] == 0) continue;
                        number = arr[j][i];
                        nx = j + dx[d];
                        ny = i + dy[d];
                    }
                    else if(d == 1){
                        if(arr[i][j] == 0) continue;
                        number = arr[i][j];
                        nx = i + dx[d];
                        ny = j + dy[d];
                    }

                    while (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                        if(arr[nx][ny] == 0){
                            arr[nx][ny] = number;
                        }
                        else if(arr[nx][ny] == arr[nx-dx[d]][ny-dy[d]]){
                            if(!flag[nx][ny]){
                                arr[nx][ny] *= 2;
                                flag[nx][ny] = true;
                                arr[nx - dx[d]][ny - dy[d]] = 0;
                                break;
                            }
                            else break;
                        }
                        else break;
                        arr[nx - dx[d]][ny - dy[d]] = 0;
                        nx += dx[d];
                        ny += dy[d];
                    }
                }
            }
        }
        else{
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    int number = 0;
                    int nx = 0;
                    int ny = 0;
                    if(d == 2) {
                        number = arr[j][i];
                        nx = j + dx[d];
                        ny = i + dy[d];
                    }
                    else if(d == 3) {
                        number = arr[i][j];
                        nx = i + dx[d];
                        ny = j + dy[d];
                    }

                    while (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                        if(arr[nx][ny] == 0){
                            arr[nx][ny] = number;
                        }
                        else if(arr[nx][ny] == arr[nx-dx[d]][ny-dy[d]]){
                            if(!flag[nx][ny]){
                                arr[nx][ny] *= 2;
                                flag[nx][ny] = true;
                                arr[nx - dx[d]][ny - dy[d]] = 0;
                                break;
                            }
                            else break;
                        }
                        else break;
                        arr[nx - dx[d]][ny - dy[d]] = 0;
                        nx += dx[d];
                        ny += dy[d];
                    }
                }
            }
        }
        return arr;

    }

    public static int calcMax(int[][] arr) {
        int tmpMax = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                tmpMax = Math.max(tmpMax, arr[i][j]);
            }
        }

        return tmpMax;
    }
}
