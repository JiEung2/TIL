//import java.io.*;
//import java.util.*;
//
//public class SWEA16811{
//    static int[] carrot;
//    static int n;
//    static List<Integer> small = new ArrayList<>();
//    static List<Integer> medium = new ArrayList<>();
//    static List<Integer> big = new ArrayList<>();
//    static int minD = Integer.MAX_VALUE;
//
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int T = Integer.parseInt(br.readLine());
//
//        for (int tc = 1; tc <= T; tc++) {
//            n = Integer.parseInt(br.readLine());
//            StringTokenizer st = new StringTokenizer(br.readLine());
//            carrot = new int[n];
//            for(int i = 0 ; i < n; i++){
//                carrot[i] = Integer.parseInt(st.nextToken());
//            }
//
//            DFS(0);
//
//            if(minD == Integer.MAX_VALUE)
//                System.out.println("#" + tc + " -1");
//            else
//                System.out.println("#" + tc + " " + minD);
//
//            small.clear();
//            medium.clear();
//            big.clear();
//            minD = Integer.MAX_VALUE;
//        }
//    }
//
//    public static void DFS(int L){
//        if(L == n){
//            int max = Math.max(small.size(), Math.max(medium.size(), big.size()));
//            int min = Math.min(small.size(), Math.min(medium.size(), big.size()));
//
//            if(max > n/2) return;
//            if(min == 0) return;
//            int tmp = max - min;
//            minD = Math.min(minD, tmp);
//
//            return;
//        }
//
//        if (!small.isEmpty() && small.get(small.size() - 1) == carrot[L])
//            small.add(carrot[L]);
//        else if (!medium.isEmpty() && medium.get(medium.size() - 1) == carrot[L])
//            medium.add(carrot[L]);
//        else if (!big.isEmpty() && big.get(big.size() - 1) == carrot[L])
//            big.add(carrot[L]);
//        else {
//            small.add(carrot[L]);
//            DFS(L + 1);
//            small.remove(small.size() - 1);
//
//            medium.add(carrot[L]);
//            DFS(L + 1);
//            medium.remove(medium.size() - 1);
//
//            big.add(carrot[L]);
//            DFS(L + 1);
//            big.remove(big.size() - 1);
//        }
//    }
//}



import java.io.*;
import java.util.*;

public class SWEA16811{
    static int[] carrot;
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            carrot = new int[n];
            int[] C = new int[31];
            for(int i = 0 ; i < n; i++){
                carrot[i] = Integer.parseInt(st.nextToken());
                C[carrot[i]] += 1;
            }
//            System.out.println(Arrays.toString(C));
            System.out.println("#" + tc + " " + check(C, n));
        }
    }

    public static int check(int[] C, int n) {
        int max = 0;
        for(int i=0; i<C.length; i++){
            if(max < C[i]) max = C[i];
        }
        System.out.println(max);
        if(max > n/2){
            return -1;
        }
        else{
            int min = n%3;
            return max - min;
        }
    }

}
