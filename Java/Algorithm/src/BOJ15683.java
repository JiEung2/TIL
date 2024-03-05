import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ15683 {
	static class Point{
		int x, y;
		public Point(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	static int n, m, cctvNum;
	static int result = Integer.MAX_VALUE;
	static List<Point> cctvList = new ArrayList<>();
	static int[] visited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		int[][] arr = new int[n][m];
		List<Point> cctv5 = new ArrayList<>();
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				if(arr[i][j] > 0 && arr[i][j] < 6) {
					if(arr[i][j] == 5) {
						cctv5.add(new Point(i, j));
					}
					else cctvList.add(new Point(i, j));
				}
			}
		}
		for(int i = 0; i < cctv5.size(); i++) {
			int x = cctv5.get(i).x;
			int y = cctv5.get(i).y;
			int[] dx = {1, 0, -1, 0};
			int[] dy = {0, -1, 0, 1};
			for(int d = 0; d < 4; d++) {
				change(x, y, dx[d], dy[d], arr);
			}
		}
		cctvNum = cctvList.size();
		visited = new int[cctvNum];
		DFS(0, arr);
		
		System.out.println(result);
		
	}
	
	public static void DFS(int L, int[][] arr) {
		if(L == cctvNum) {
			count(arr);
			return;
		}
		

		int x = cctvList.get(L).x;
		int y = cctvList.get(L).y;
		int[] dx = {1, 0, -1, 0};
		int[] dy = {0, -1, 0, 1};
		if(arr[x][y] == 1) {
			for(int d = 0; d < 4; d++) {
				int[][] tmp = copyArr(arr);
				change(x, y, dx[d], dy[d], tmp);
				DFS(L + 1, tmp);
			}
		}
		else if(arr[x][y] == 2) {
			for(int d = 0; d < 2; d++) {
				int[][] tmp = copyArr(arr);
				change(x, y, dx[d], dy[d], tmp);
				change(x, y, dx[d+2], dy[d+2], tmp);
				DFS(L + 1, tmp);
			}
		}
		else if(arr[x][y] == 3) {
			for(int d = 0; d < 4; d++) {
				int[][] tmp = copyArr(arr);
				change(x, y, dx[d], dy[d], tmp);
				change(x, y, dx[(d+1)%4], dy[(d+1)%4], tmp);
				DFS(L + 1, tmp);
			}
		}
		else if(arr[x][y] == 4) {
			for(int d = 0; d < 4; d++) {
				int[][] tmp = copyArr(arr);
				change(x, y, dx[d], dy[d], tmp);
				change(x, y, dx[(d+1)%4], dy[(d+1)%4], tmp);
				change(x, y, dx[(d+2)%4], dy[(d+2)%4], tmp);
				DFS(L + 1, tmp);
			}
		}
		
	}
	
	public static void count(int[][] arr) {
		int cnt = 0;
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				if(arr[i][j] == 0) {
					cnt++;
				}
			}
		}
//		if(result > cnt) {
//			result = cnt;
//			for(int i = 0; i < n; i++) {
//				for(int j = 0; j < m; j++) {
//					System.out.print(arr[i][j] + " ");
//				}
//				System.out.println();
//			}
//		}
		result = Math.min(result, cnt);
	}
	
	public static int[][] copyArr(int[][] arr) {
		int[][] tmp = new int[n][m];
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				tmp[i][j] = arr[i][j];
			}
		}
		return tmp;
	}
	
	public static void change(int x, int y, int dx, int dy, int[][] arr) {
		int nx = x + dx;
		int ny = y + dy;
		
		while(nx >= 0 && nx < n && ny >= 0 && ny < m && (arr[nx][ny] < 6 || arr[nx][ny] == -1)) {
			if(!(arr[nx][ny] > 0 && arr[nx][ny] < 6)) {
				arr[nx][ny] = -1;
			}
			nx += dx;
			ny += dy;
		}
	}
	
}
