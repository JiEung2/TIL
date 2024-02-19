# BFS

## 그래프 탐색(순회)
- 그래프 순회는 비선형구조인 그래프로 표현된 모든 자료(정점)를 빠짐없이 탐색하는 것을 의미한다.
- 두 가지 방법
    - 너비 우선 탐색(Breadth First Search, BFS)
    - 깊이 우선 탐색(Depth First Search, DFS)

## BFS
- 너비우선탐색은 `탐색 시작점`의 `인접한 정점들`을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
- 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐를 활용함

### BFS 알고리즘
- 그래프
    ```
    BFS(v) // 탐색 시작 정점 v
        큐 생성
        시작 정점 v를 큐에 삽입
        정점 v를 방문한 것으로 표시
        while(큐가 비어 있지 않은 경우){
            t <- 큐의 첫 번째 원소 반환
            for(t와 연결된 모든 간선에 대해){
                u <- t의 인점 정점
                u가 방문되지 않은 곳이면,
                u를 큐에 넣고, 방문한 것으로 표시
            }
        } 

    ```

- 트리
    ```
    BFS()
        큐 생성
        루트 v를 큐에 삽입
        while(큐가 비어 있지 않은 경우) {
            t <- 큐의 첫 번째 원소 반환

            for(t와 연결된 모든 간선에 대해) {
                u <- t의 자식노드
                u를 큐에 삽입
            }
        }
    ```

## 너비 우선 탐색 - 인접 행렬
```java
static void bfs(int[][] adjMatrix, int start){
    int V = adjMatrix.length;

    Queue<Integer> queue = new ArrayDeque<>();
    boolean[] visited = new boolean[V];

    queue.offer(start);
    visited[start] = true;

    while(!queue.isEmpty()){
        int current = queue.poll();
        System.out.println((char)(current+65));
        for(int i = 0 ; i < V; i++){
            if(adjMatrix[current][i] != 0   // 인접정점 체크
                && !visited[i]){    // 방문 여부 체크
                    queue.offer(i);
                    visited[i] = true;
                }
        }
    }
}
```

## 너비 우선 탐색 - 인접 리스트
```java
static void bfs(Node[] adjList, int start){
    int V = adjMatrix.length;

    Queue<Integer> queue = new ArrayDeque<>();
    boolean[] visited = new boolean[V];

    queue.offer(start);
    visited[start] = true;

    while(!queue.isEmpty()){
        int current = queue.poll();
        System.out.println((char)(current+65));
        for(Node temp=adjList[current]; temp != null; temp = temp.next){
            if(!visited[temp.to]){    // 방문 여부 체크
                    queue.offer(temp.to);
                    visited[temp.to] = true;
                }
        }
    }
}
```

## 너비 우선 탐색 - 최단 경로