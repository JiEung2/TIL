//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//import java.util.ArrayList;
//import java.util.List;
//import java.util.StringTokenizer;
//
//public class SWEA1767 {
//    static class Point {
//        public int x, y;
//        public Point(int x, int y){
//            this.x = x;
//            this.y = y;
//        }
//    }
//    static int[][] arr;
//    static int n, num, result;
//    static List<Point> cpuList;
//    static int[] check;
//    static int[] dx = {1, 0, -1, 0};
//    static int[] dy = {0, 1, 0, -1};
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int T = Integer.parseInt(br.readLine());
//
//        for(int tc = 0; tc < T; tc++){
//            n = Integer.parseInt(br.readLine());
//            arr = new int[n][n];
//            num = 0;
//            result = Integer.MAX_VALUE;
//            cpuList = new ArrayList<>();
//            for(int i = 0 ; i < n; i++){
//                StringTokenizer st = new StringTokenizer(br.readLine());
//                for(int j = 0; j < n; j++){
//                    arr[i][j] = Integer.parseInt(st.nextToken());
//                    if(arr[i][j] == 1) {
//                        num++;
//                        if(i == 0 || j == 0) continue;
//                        cpuList.add(new Point(i, j));
//                    }
//                }
//            }
//            check = new int[num-cpuList.size()];
//
//        }
//    }
//
//    public static void combi(int limit, int L, int index) {
//        if(limit == L){
//            dfs(0, 0);
//            return;
//        }
//        for(int i = 0; i < num-cpuList.size(); i++){
//            check[i] = 1;
//            combi(limit, L + 1, index + 1);
//            check[i] = 0;
//        }
//    }
//
//    public static void dfs(int L, int cnt){
//        if (L == num - cpuList.size()) {
//            result = Math.min(result, cnt);
//        }
//        if ()
//
//        for(int i = 0; i < 4; i++){
//
//        }
//    }
//}
