# 최소 신장 트리(MST)

- 그래프에서 최소 비용 문제
    1) 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리
    2) 두 정점 사이의 최소 비용의 경로 찾기

- 신장 트리
    - n개의 정점으로 이루어진 무향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리

- 최소 신장 트리 (Minimum Spanning Tree)
    - 무향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리

## KRUSKAL 알고리즘(-> 간선중심 해결)
- 간선을 하나씩 선택해서 MST를 찾는 알고리즘
    1) 최초, 모든 간선을 가중치에 따라 오름차순으로 정렬
    2) 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가시킴
        - 사이클이 존재하면 남아 있는 간선 중 그 다음으로 가중치가 낮은 간선 선택
    3) n-1개의 간선이 선택될 때 2를 반복

- 알고리즘
```
// G.V: 그래프의 정점 집합, G.E: 그래프의 간선 집합
// n: 정점 수, cnt: 선택한 간선 수, weight: 선택한 간선들의 가중치 합
MST-KRUSKAL(G, W)
    cnt = 0, weight = 0
    FOR vertex v in G.V
        Make-set(v)
    End FOR
    FOR 간선 (u, v) of G.E 선택
        IF Find-Set(u) != Find-Set(v) THEN
            Union(u, v)
            cnt = cnt + 1
            weight = weight + w
            IF cnt == n-1 THEN
                break
            END IF
        END IF
    END FOR
END MST-KRUSKAL()
```

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class MST_TEST {
    public static Edge[] getEdgeList() {
        return edgeList;
    }

    static class Edge implements Comparable<Edge> {
        int from, to, weight;

        public Edge(int from, int to, int weight) {
            super();
            this.from = from;
            this.to = to;
            this.weight = weight;
        }

        @Override
        public int compareTo(Edge o) {
            return Integer.compare(this.weight, o.weight);
        }
    }

    static int V;
    static Edge[] edgeList;
    static int[] parents;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        edgeList = new Edge[E];

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            edgeList[i] = new Edge(from, to, weight);
        } // 간선리스트 생성

        // 전처리: 간선 리스트 오름차순 정렬
        Arrays.sort(edgeList);

        // 1. make - set
        make();

        // 2. 정렬된 간선 하나씩 꺼내어 신장 트리 생성
        int weight = 0;
        int cnt = 0;
        for (Edge edge : edgeList) {
            if(!union(edge.from, edge.to)) continue; // 싸이클 발생
            weight += edge.weight;
            if(++cnt==V-1) break; // 최소신장트리 완성
        }
        System.out.println(weight);
    }

    public static void make() {
        parents = new int[V]; // 자신의 부모나 루트를 저장(경로 압축으로 인해)
        for (int i = 0; i < V; i++) {
            parents[i] = i; // 모든 정점을 자신의 대표자(루트)로
        }
    }

    public static int find(int a){ // a가 속한 트리의 추트 찾기
        if(a == parents[a]) return a;

        return parents[a] = find(parents[a]);
    }

    public static boolean union(int a, int b) {
        int aRoot = find(a);
        int bRoot = find(b);
        if(aRoot == bRoot) return false; // a,b가 같은 트리에 속해있다. --> union 불필요

        parents[bRoot] = aRoot;
        return true;
    }


}
```

## PRIM 알고리즘(-> 정점중심 해결 => 그래프: 인접행렬 or 인접리스트)
- 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식
    1) 임의 정점을 하나 선택해서 시작
    2) 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택
    3) 모든 정점이 선택될 때 까지 2 과정을 반복

- 서로소인 2개의 집합(2 disjoint-sets) 정보를 유지
    - 트리 정점들(tree vertices) - MST를 만들기 위해 선택된 정점들
    - 비트리 정점들(non-tree vertices) - 선택 되지 않은 정점들