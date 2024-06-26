# 트리

- 트리의 개념
    - 비선형 구조
    - 원소들 간에 1:n 관계를 가지는 자료구조
    - 원소들 간에 계층관계를 가지는 계층형 자료구조
    - 상위 원소에서 하위 원소로 내려가면서 확장되는 트리(나무)모양의 구조
    - ex) 파일 시스템 디렉토리 구조, 가계도, 조직도 등

## 트리 - 정의
- 노드(node) - 트리의 원소
- 한 개 이상의 노드로 이루어진 유한 집합이며 다음 조건을 만족함
    1) 노드 중 최상위 노드를 루트(root)라 함
    2) 나머지 노드들은 n(>=0)개의 분리 집합 T1,...,TN으로 분리될 수 있다.
- 이들 T1,...,TN은 각각 하나의 트리가 되며(재귀적 정의) 루트의 부 트리(subtree)라 함
- 간선(edge) - 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
- 서브트리(subtree) - 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- 자손 노드 - 서브 트리에 있는 하위 레벨의 노드들

- 차수(degree)
    - 노드의 차수: 노드에 연결된 자식 노드의 수(B의 차수=2, C의 차수=1)
    - 트리의 차수: 트리에 있는 노드의 차수 중에서 가장 큰 값(트리 T의 차수 = 3)
    - 단말 노드(리프 노드): 차수가 0인 노드 즉, 자식 노드가 없는 노드

- 높이
    - 노드의 높이: 루트에서 노드에 이르는 간선의 수. 노드의 레벨(B의 높이 = 1, F의 높이 = 2)
    - 트리의 높이: 트리에 있는 노드의 높이 중에서 가장 큰 값. 최대 레벨(트리 T의 높이=3)

### 이진 트리
- 차수가 2인 트리
- 각 노드가 자식 노드를 최대한 2개 까지만 가질 수 있는 트리 (간선 최대 2개까지만)
    - 왼쪽 자식 노드(left child node)
    - 오른쪽 자식 노드(right child node)
- 모든 노드들 이 최대 2개의 서브트리를 갖는 특별한 형태의 트리

### 이진트리 - 특성
- 높이 i(레벨 i)에서의 노드의 최대 개수는 2^i개
- 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 `(h+1)`개가 되며, 최대 개수는 `(2^(h+1)-1)`개가 됨

### 이진 트리 - 종류
- 포화 이진 트리(Perfect Binary Tree)
    - 모든 레벨에 노드가 포화 상태로 차 있는 이진 트리
    - 높이가 h일 때, 최대의 노드 개수인 (2^(h+1)-1)의 노드를 가진 이진 트리
        - 높이가 3일 때 2^(3+1)-1 = 15개 노드
    - 루트를 1번으로 하여 2^(h+1)-1까지 정해진 위치에 대한 노드 번호를 가짐

- 완전 이진 트리(Complete Binary Tree)
    - 높이가 h이고 노드 수가 n개일 때 (단, h+1 <= n < 2^(h+1)-1), 포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리

- 편향 이진 트리(Skewed Binary Tree)
    - 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드 만을 가진 이진 트리
        - 왼쪽 편향 이진 트리
        - 오른쪽 편향 이진 트리


## 트리 탐색 - DFS
### DFS(Depth First Search)
- 깊이 우선 탐색
- 루트 노드에서 출발하여 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 노드로 되돌아와서 다른 방향의 노드로 탐색을 계속 반복하여 결국 모든 노드를 방문하는 순회방법
- 가장 마지막에 만났던 갈림길의 노드로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 재귀적으로 구현하거나 후입선출 구조의 스택 사용해서 구현 

### DFS 예
1) 루트노드 A를 시작으로 깊이 우선 탐색을 시작
```
DFS(A)
    A 방문;

    //A의 자식노드(B,C,D) 모두에 대하여
    DFS(B)
    DFS(C)
    DFS(D)
```  
2) 노드 B에서 깊이 우선 탐색 처리
3) 노드 E에서 깊이 우선 탐색 처리 -> 리프노드라서 리턴
4) 노드 F에서 깊이 우선 탐색 처리
5) 노드 C에서 깊이 우선 탐색 처리  
...
![Alt text](Tree2-1.png)
=> 탐색순서: A B E F C D G H I

### 이진트리
### 이진트리 - 순회(traversal)
- 순회(traversal): 트리의 노드들을 체계적으로 방문하는 것
- 3가지의 기본적인 순회방법
    - 전위순회(preorder traversal): VLR
        - 부모 노드 방문 후, 자식노드를 좌,우 순서로 방문
    - 중위순회(inorder traversal): LVR
        - 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문
    - 후위순회(postorder traversal): LRV
        - 자식노드를 좌우 순서로 방문한 후, 부모노드로 방문



![Alt text](Tree2-2.png)  
- 전위순회  
    -> 총 순서: A B D H I E C F G
- 중위순회  
    -> 총 순서: H D I B E A F C G
- 후위순회
    -> 총 순서: H I D E B F G C A

### 수식트리
- 수식을 표현하는 이진트리
- 수식 이진 트리 (Expression Binary Tree)라고 부르기도 함.
- 연산자는 루트 노드이거나 가지 노드
- 피연산자는 모두 잎 노드

## 힙(heap)
- 완전 이진 트리에 있는 노드 중에서 키 값이 가장 큰 노드나 키 값이 가장 작은 노드를 찾기 위해서 만든 자료구조
- 최대 힙(max heap)
    - 키 값이 가장 큰 노드를 찾기 위한 완전 이진 트리
    - 부모 노드의 키 값 >= 자식 노드의 키 값
    - 루트 노드: 키 값이 가장 큰 노드
- 최소 힙(min heap)
    - 키 값이 가장 작은 노드를 찾기 위한 완전 이진 트리
    - 부모 노드의 키 값 =< 자식 노드의 키 값
    - 루트 노드: 키 값이 가장 작은 노드

![Alt text](Tree2-3.png)

### 힙 연산 - 삽입
- 최대 힙에서 23 삽입  
![Alt text](Tree2-4.png)

### 힙 연산 - 삭제
- 힙에서는 루트 노드의 원소만을 삭제할 수 있음
- 루트 노드의 원소를 삭제하여 반환
- 힙의 종류에 따라 최대값 또는 최소값을 구할 수 있음  
![Alt text](Tree2-5.png)