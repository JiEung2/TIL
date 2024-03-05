import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ15686 {
	static class Point {
		int x, y;
		public Point(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	static int n,m;
	static int result = Integer.MAX_VALUE;
	static int[][] arr;
	static int[] visited;
	static List<Point> house = new ArrayList<>();
	static List<Point> chicken = new ArrayList<>();
	

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		arr = new int[n][n];
		
		
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < n; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				if(arr[i][j] == 1) house.add(new Point(i, j));
				else if(arr[i][j] == 2) chicken.add(new Point(i ,j));
			}
		}
		visited = new int[chicken.size()];
		
		DFS(0, 0);
		
		System.out.println(result);
	}
	
	private static void DFS(int L, int index) {
		if(L == m) {
			calc();
			return;
		}
		
		for(int i = index; i < chicken.size(); i++) {
			if(visited[i] == 0) {
				visited[i] = 1;
				DFS(L+1, i + 1);
				visited[i] = 0;
			}
		}
		
	}
	
	private static void calc() {
		int totalSum = 0;
		for(int i = 0; i < house.size(); i++) {
			int sum = Integer.MAX_VALUE;
			Point h = house.get(i);
			for(int j = 0; j < chicken.size(); j++) {
				Point c = chicken.get(j);
				if(visited[j] == 1) {
					int dis = Math.abs(h.x - c.x) + Math.abs(h.y - c.y);
					sum = Math.min(sum, dis);
				}
			}
			totalSum += sum;
		}
		result = Math.min(result, totalSum);
	}

}
