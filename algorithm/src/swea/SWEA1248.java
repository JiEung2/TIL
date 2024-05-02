package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.Array;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;


public class SWEA1248 {
    static int V, E, a, b;
    static int cnt;
    static List<List<Integer>> graph;
    static int[] nodes;
    static int visited[];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int tc = 1; tc <= T; tc++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            V = Integer.parseInt(st.nextToken());
            E = Integer.parseInt(st.nextToken());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());

            nodes = new int[V+1];
            graph = new ArrayList<>();
            cnt = 1;
            visited = new int[V+1];
            for(int i = 0; i <= V; i++){
                graph.add(new ArrayList<>());
            }
            st = new StringTokenizer(br.readLine());
            for(int i = 0; i < E; i++){
                int parent = Integer.parseInt(st.nextToken());
                int child = Integer.parseInt(st.nextToken());
                nodes[child] = parent;
                graph.get(parent).add(child);
            }

            int sameParent = 0;

            while(a != 0){
                visited[a] = 1;
                a = nodes[a];
            }

            while(b != 0){
                if (visited[b] == 1) {
                    sameParent = b;
                    break;
                }
                b = nodes[b];
            }
            cnt = countSubtreeSize(sameParent);
            System.out.println("#" + tc + " "+sameParent + " " + cnt);
        }
    }

    public static int countSubtreeSize(int root){
        int size = 1;
        for (int child : graph.get(root)) {
            size += countSubtreeSize(child);
        }
        return size;
    }

}
