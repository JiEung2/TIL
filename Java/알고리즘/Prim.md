# Prim 알고리즘

- 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식  
    1) 임의 정점을 하나 선택해서 시작
    2) 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택
    3) 모든 정점이 선택될 때까지 2의 과정을 반복
    
- 서로소인 2개의 집합(2 disjoint-sets) 정보를 유지
    - 트리 정점들(tree vertices) - MST를 만들기 위해 선택된 정점들
    - 비트리 정점들(non-tree vertices) - 선택 되지 않은 정점들
    
### 알고리즘
```
// G: 그래프, r: 시작 정점, minEdge[]: 각 정점기준으로 타 정점과의 최소 간선 비용
MST-PRIM(G, r)
    result = 0, cnt = 0     // result: MST비용, cnt: 처리한 정점 수, visited[]: MST에 포함된 정점 여부
    FOR u in G.V
        minEdge[u] = 무한대
    minEdge[r] = 0                          // 시작 정점 r의 최소비용 0 처리
    WHILE true
        u = Extract-MIN()                   // 방문하지 않은(MST에 포함되지 않은 정점) 최소 간선 비용 정점 찾기
        visited[u] = true                   // 방문 처리
        result = result + minEdge[u];       // 모든 정점이 다 연결되었으면 MST 완성
        FOR v in G.Adj[u]                   // u의 인접 정점들
            // 미방문 정점 중 u -> v 비용이 minEdge[v]보다 작다면 갱싱
            IF visited[v] == false AND w(u, v) < minEdge[v] THEN
                minEdge[v] = w(u, v)
            END IF
        END FOR
    END WHILE
END MST-PRIM()   
```

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class PrimTest {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int V = Integer.parseInt(br.readLine());
        int[][] adjMatrix = new int[V][V]; // 인접행렬 준비
        boolean[] visited = new boolean[V]; // 트리 정점 여부
        int[] minEdge = new int[V]; //비트리정점 기준으로 트리정점들과 연결했을 경우 최소 간선 비용

        StringTokenizer st = null;
        for (int i = 0; i < V; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < V; j++) {
                adjMatrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        Arrays.fill(minEdge, Integer.MAX_VALUE); // 최소값 갱신을 위해 max로 초기화
        minEdge[0] = 0; // 임의의 시작점 0을 위해 처리
        int result = 0; // 최소신장트리 비용

        int i;
        for (i = 0; i < V; i++) {
            // step 1: 비트리 정점 중 최소간선비용의 정점 찾기
            int min = Integer.MAX_VALUE;
            int minVertex = -1;

            for(int j = 0; j <V; j++){
                if (!visited[j] && minEdge[j] < min) {
                    min = minEdge[i];
                    minVertex = i;
                }
            }

            if(minVertex == -1) break;
            result += min; // 간선 비용 누적
            visited[minVertex] = true; // 트리 정점에 포함

            // step 2: 새롭게 트리 정점에 확장된 정점 기준으로 비트리 정점들과의 간선비용 고려 최적 업데이트
            for(int j = 0; j < V; j++){
                if (!visited[j] && adjMatrix[minVertex][j] != 0 && adjMatrix[minVertex][j] < minEdge[j]) {
                    minEdge[j] = adjMatrix[minVertex][j];
                }
            }
        }
        System.out.println(i == V ? result : -1);
    }
}
```

### PRIM 알고리즘 with PriorityQueue(Heap: 최소, 최대 값 빠르게 탐색)
- 알고리즘
```
MST-PRIM(G, r)
    result <- 0, cnt <- 0
    FOR u in G.V
        minEdge[u] <- 무한대
    minEdge[r] <- 0
    WHILE true
        u <- extract - MIN()    // 방문하지 않은(MST에 포함되지 않은 정점) 최소비용 정점 찾기
        ...                     // => PQ 준비, 비트리정점 중 트리 정점 간선 비용 업데이트 될 때마다 PQ에 넣기
    return result
END MST-PRIM()
```

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class PrimPQTest {

    static class Vertex implements Comparable<Vertex>{
        int no, weight;

        public Vertex(int no, int weight) {
            this.no = no;
            this.weight = weight;
        }


        @Override
        public int compareTo(Vertex o) {
            return Integer.compare(this.weight, o.weight);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int V = Integer.parseInt(br.readLine());
        int[][] adjMatrix = new int[V][V]; // 인접행렬 준비
        boolean[] visited = new boolean[V]; // 트리 정점 여부
        int[] minEdge = new int[V]; //비트리정점 기준으로 트리정점들과 연결했을 경우 최소 간선 비용

        StringTokenizer st = null;
        for (int i = 0; i < V; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < V; j++) {
                adjMatrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        PriorityQueue<Vertex> pq = new PriorityQueue<>(); //---------------------
        Arrays.fill(minEdge, Integer.MAX_VALUE); // 최소값 갱신을 위해 max로 초기화
        minEdge[0] = 0; // 임의의 시작점 0을 위해 처리
        pq.offer(new Vertex(0, minEdge[0]));

        int result = 0; // 최소신장트리 비용
        int i = 0;
        while (!pq.isEmpty()) {

            // step 1: 비트리 정점 중 최소간선비용의 정점 찾기
            Vertex minVertex = pq.poll();
            if(visited[minVertex.no]) continue;

            result += minVertex.weight; // 간선 비용 누적
            visited[minVertex.no] = true; // 트리 정점에 포함
            if(++i == V) break;

            // step 2: 새롭게 트리 정점에 확장된 정점 기준으로 비트리 정점들과의 간선비용 고려 최적 업데이트
            for(int j = 0; j < V; j++){
                if (!visited[j] && adjMatrix[minVertex.no][j] != 0
                        && adjMatrix[minVertex.no][j] < minEdge[j]) {
                    minEdge[j] = adjMatrix[minVertex.no][j];
                    pq.offer(new Vertex(j, minEdge[j]));
                }
            }
        }
        System.out.println(i == V ? result : -1);
    }
}

```