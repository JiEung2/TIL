import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ3190 {
    static int board[][];
    static int[] move;
    static char[] d;
    static int n, k, l;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());

        board = new int[n][n];

        for (int i = 0; i < k; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            board[r-1][c-1] = 1;
        }

        l = Integer.parseInt(br.readLine());
        move = new int[l];
        d = new char[l];
        for (int i = 0; i < l; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            move[i] = Integer.parseInt(st.nextToken());
            d[i] = st.nextToken().charAt(0);
        }

        int result = start();
        System.out.println(result);
    }

    public static int start(){
        int dx[] = {-1, 0, 1, 0};
        int dy[] = {0, 1, 0, -1};
        int second = 0;
        int dir = 1;
        int x = 0, y = 0;
        board[x][y] = 2;
        int[] tail = {0, 0};
        int[][] check = new int[n][n];
        int i = 0;

        while (true) {
            second++;
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if(nx >= 0 && nx < n && ny >= 0 && ny < n && board[nx][ny] != 2){
                check[x][y] = dir;
                if(board[nx][ny] == 0) {
                    board[tail[0]][tail[1]] = 0;
                    int tmp = check[tail[0]][tail[1]];
                    tail[0] += dx[tmp];
                    tail[1] += dy[tmp];
                }
                board[nx][ny] = 2;
                x = nx;
                y = ny;

            }
            else return second;
            if(i < l && second == move[i]){
                if(d[i] == 'D'){
                    dir = (dir + 1) % 4;
                }
                else{
                    if (dir == 0) {
                        dir = 3;
                    }
                    else dir--;
                }
                i++;
            }
        }
    }
}
