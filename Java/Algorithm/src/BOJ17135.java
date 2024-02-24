import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ17135 {
	static class Point{
		int x, y;
		
		public Point(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	
	static int n, m, d, result;
	static int[][] board;
	static Point[] archer;
	static int[] checked;
	static int[][] game_board;
	static Point[] kill_list;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		d = Integer.parseInt(st.nextToken());
		board = new int[n][m];
		checked = new int[m];
		result = 0;
		
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < m; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		archer = new Point[3];
		DFS(0);
		System.out.println(result);
		
	}
	
	public static void DFS(int L) {
		if(L == 3) {
			gameStart();
			return;
		}
		
		for(int i = 0; i < m; i++) {
			if(checked[i] == 0){
				checked[i] = 1;
				archer[L] = new Point(n, i);
				DFS(L+1);
				checked[i] = 0;
			}
		}
	}
	
	public static void gameStart() {
		int cnt = 0;
		game_board = new int[n][m];
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				game_board[i][j] = board[i][j];
			}
		}

		while(true) {
			kill_list = new Point[3];
			for(int i = 0; i < 3; i++) {
				int x = archer[i].x;
				int y = archer[i].y;
				kill_list[i] = makeKillList(x, y);
			}
			cnt += kill();
			boolean flag = true;
			for(int i = n-1; i >= 0; i--) {
				for(int j = m-1; j >= 0; j--) {
					if(game_board[i][j] == 1) {
						flag = false;
						if(i != n-1) {
							game_board[i+1][j] = 1;
						}
						game_board[i][j] = 0;
					}
				}
			}
			if(flag) {
				result = Math.max(result, cnt);
				break;
			}
		}
	}
	
	public static int kill() {
		int count = 0;
		for(int i = 0; i < 3; i++) {
			int x = kill_list[i].x;
			int y = kill_list[i].y;
			if(x != -1) {
				if(game_board[x][y] == 1) {
					game_board[x][y] = 0;
					count++;
				}
			}
		}
		
		return count;
	}
	
	public static Point makeKillList(int x, int y) {
		int minDis = Integer.MAX_VALUE;
		int minX = -1;
		int minY = -1;
		for(int i = 0; i < m; i++) {
			for(int j = 1; j <= d; j++) {
				if(n-j >= 0) {
					int dis = Math.abs(x - (n-j)) + Math.abs(y - i);
					if(game_board[n-j][i] == 1 && dis <= d) {
						if(dis < minDis) {
							minDis = dis;
							minX = n-j;
							minY = i;
						}
					}
				}
			}
		}
		return new Point(minX, minY);
	}
	

}
