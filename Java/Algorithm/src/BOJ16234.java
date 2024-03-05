import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ16234 {
	static int n, L, R, flag;
	static int[][] visited;
	static int[] dx = {1, 0, -1, 0};
	static int[] dy = {0, 1, 0, -1};
	static int[][] nation;
	static int[] sum;
	static int[] cnt;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		L = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());
		
		nation = new int[n][n];
		
		
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < n; j++) {
				nation[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int result = 0;
		while(true) {
			flag = 0;
			visited = new int[n][n];
			sum = new int[n*n + 1];
			cnt = new int[n*n + 1];
			for(int i = 0; i <n; i++) {
				for(int j =0; j<n; j++) {
					DFS(i, j);
				}
			}
			if(flag == n*n) break;
			
			merge();
			result++;
		}
		
		System.out.println(result);
		
	}
	
	static void DFS(int i, int j) {
		if(visited[i][j] == 0) {
			flag++;
			visited[i][j] = flag;
			sum[flag] += nation[i][j];
			cnt[flag]++;
		}
		for(int d = 0; d < 4; d++) {
			int nx = i + dx[d];
			int ny = j + dy[d];
			
			if(nx >= 0 && nx < n && ny >= 0 && ny < n 
					&& visited[nx][ny] == 0 && Math.abs(nation[i][j] - nation[nx][ny]) >= L 
					&& Math.abs(nation[i][j] - nation[nx][ny]) <= R) {
				visited[nx][ny] = flag;
				sum[flag] += nation[nx][ny];
				cnt[flag]++;
				DFS(nx, ny);
			}
		}
		
	}
	
	static void merge() {
		for(int d = 1; d <= flag; d++) {
			int people = sum[d] / cnt[d];
			
			for(int i = 0; i<n; i++) {
				for(int j = 0; j<n; j++) {
					if(visited[i][j] == d) {
						nation[i][j] = people;
					}
				}
			}
		}
	}
	
	static class Point{
		int x, y;
		public Point(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

}
