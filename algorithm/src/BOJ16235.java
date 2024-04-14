import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ16235 {
    static class Tree{
        int x, y, z;
        boolean dead=false;

        public Tree(int x, int y, int z){
            this.x = x;
            this.y = y;
            this.z = z;
        }
    }
    static int[][] land, og;
    static int n, m, k;
    static List<Tree> treeList = new ArrayList<>();
    static Queue<Tree> deadTreeList = new LinkedList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        land = new int[n][n];
        og = new int[n][n];
        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0 ; j < n; j++){
                land[i][j] = 5;
                og[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int z = Integer.parseInt(st.nextToken());
            treeList.add(new Tree(x-1, y-1, z));
        }

        Collections.sort(treeList, (t1, t2) -> t1.z - t2.z);

        for(int i = 0; i < k; i++){
            spring();
            summer();
            fall();
            winter();
        }

        System.out.println(treeList.size());
    }

    public static void spring(){
        for(int i = 0; i < treeList.size(); i++){
            Tree tree = treeList.get(i);
            if(tree.z <= land[tree.x][tree.y]){
                land[tree.x][tree.y] -= tree.z;
                tree.z++;
            }
            else{
                tree.dead = true;
                deadTreeList.add(tree);
            }
        }

    }

    public static void summer(){
        while(!deadTreeList.isEmpty()) {
            Tree tree = deadTreeList.poll();
            land[tree.x][tree.y] += tree.z / 2;
        }
    }

    public static void fall(){
        List<Tree> newTree = new ArrayList<>();

        int[] dx = {1, 0, -1, 0, -1, -1, 1, 1};
        int[] dy = {0, -1, 0, 1, -1, 1, -1, 1};
        for(int i = 0; i < treeList.size(); i++){
            Tree tree = treeList.get(i);
            if (tree.dead) continue;;
            if (tree.z % 5 == 0) {
                for(int j = 0; j < 8; j++){
                    int nx = tree.x + dx[j];
                    int ny = tree.y + dy[j];
                    if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                        newTree.add(new Tree(nx, ny, 1));
                    }
                }
            }
        }
        for (int i = 0; i < treeList.size(); i++) {
            Tree tree = treeList.get(i);
            if (!tree.dead) {
                newTree.add(tree);
            }
        }
        treeList = newTree;
    }

    public static void winter(){
        for(int i = 0 ; i < n; i++){
            for(int j = 0; j < n; j++){
                land[i][j] += og[i][j];
            }
        }
    }
}
