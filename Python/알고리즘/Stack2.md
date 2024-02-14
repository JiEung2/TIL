# Stack2

## 계산기1
- 문자열로 된 계산식이 주어질 때, 스택을 이용하여 이 계산식의 값을 계산할 수 있다.
- 문자열 수식 계산의 일반적 방법
    - step1. 중위 표기법의 수식을 후위 표기법으로 변경(스택 이용)
    ```
    중위표기법(infix notation)
    - 연산자를 피연산자의 가운데 표기하는 방법
        예) A + B
    
    후위표기법(postfix notation)
    - 연산자를 피연산자 뒤에 표기하는 방법
        예) AB+
    ```
    - step2. 후위 표기법의 수식을 스택을 이용하여 계산

- step1 -> 중위표기식의 후위표기식 변환 방법1
    - 수식의 각 연산자에 대해서 우선순위에 따라 괄호를 사용하여 다시 표현
    - 각 연산자를 그에 대응하는 오른쪽괄호의 뒤로 이동시킴
    - 괄호 제거
- step1 -> 중위표기법에서 후위표기법으로의 변환 알고리즘(스택 이용)2
    1) 입력받은 중위 표기식에서 토큰을 읽음
    2) 토큰이 피연산자이면 토큰을 출력
    3) 토큰이 연산자(괄호포함)일 때, 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push하고, 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop한 후 토큰의 연산자를 push 함. 만약 top에 연산자가 없으면 push
    4) 토큰이 오른쪽 괄호')'이면 스택 top에 왼쪽 괄호'('가 올 때까지 스택에 pop 연산을 수행하고 pop한 연산자를 출력. 왼쪽 괄호를 만나면 pop만 하고 출력하지는 않음
    5) 중위 표기식에 더 읽을 것이 없다면 중지하고, 더 읽을 것이 있다면 1부터 다시 반복
    6) 스택에 남아 있는 연산자를 모두 pop하여 출력
        - 스택 밖의 왼쪽 괄호는 우선 순위가 가장 높으며, 스택 안의 왼쪽 괄호는 우선순위가 가장 낮음

## 계산기2
- step2. 후위 표기법의 수식을 스택을 이용하여 계산
    1) 피연산자를 만나면 스택에 push
    2) 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산결과를 다시 스택에 push
    3) 수식이 끝나면, 마지막으로 스택을 pop하여 출력

## 백트래킹
- 백트래킹(Backtracking) 기법은 해를 찾는 도중에 '막히면' (즉, 해가 아니면) 되돌아가서 다시 해를 찾아가는 기법
- 백트래킹 기법은 최적화(optimization) 문제와 결정(decision) 문제를 해결할 수 있음
- 결정 문제: 문제의 조건을 만족하는 해가 존재하는지의 여부를 'yes' 또는 'no'가 답하는 문제
    - 미로 찾기
    - n-Queen 문제
    - Map coloring
    - 부분 집합의 합(Subset Sum) 문제 등

### 백트래킹: 미로 찾기
- 입구와 출구가 주어진 미로에서 입구부터 출구까지의 경로를 찾는 문제
- 이동할 수 있는 방향은 4방향으로 제한


### 백트래킹과 깊이우선탐색과의 차이
- 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임. (Punning 가지치기)
- 깊이우선탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단
- 깊이우선탐색을 가하기에는 경우의 수가 너무나 많음. 즉, N! 가지의 경우의 수를 가진 문제에 대해 깊이우선탐색을 가하면 당연히 처리 불가능한 문제
- 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간(Exponential Time)을 요하므로 처리 불가능

- 모든 후보를 검사? -> No!
- 백트래킹 기법
    - 어떤 노드의 유망성을 점검한 후에 유망(promising)하지 않다고 결정되면 그 노드의 부모로 되돌아가(backtracking) 다음 자식 노드로 감
    - 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 함
    - 가지치기(prunning): 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않음

- 백트래킹을 이용한 알고리즘은 다음과 같은 절차로 진행됨
    1) 상태 공간 트리의 깊이 우선 검색을 실시
    2) 각 노드가 유망한지를 점검
    3) 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속함

- 일반 백트래킹 알고리즘
    ```
    def checknode(v):
        if promising(v):
            if there is a solution at v:
                write the solution
            else:
                for u in each child of v:
                    checknode(u)
    ```

### 부분집합
- 어떤 집합의 공집합과 자기자신을 포함한 모든 부분집합을 powerset이라고 하며 구하고자 하는 어떤 집합의 원소 개수가 n일 경우 부분집합의 개수는 2^n개이다.
- 백트래킹 기법으로 powerset을 만들어보자.
    - 앞에서 설명한 일반적인 백트래킹 접근 방법을 이용
    - n개의 원소가 들어있는 집합의 2^n개의 부분집합을 만들 때는, true 또는 false값을 가지는 항목들로 구성된 n개의 배열을 만드는 방법을 이용
    - 여기서 배열의 i번째 항목은 i번째의 원소가 부분집합의 값인지 아닌지를 나타내는 값

- 각 원소가 부분집합에 포함되었는지를 loop 이용하여 확인하고 부분집합을 생성하는 방법
```
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i              # 0번째 원소
    for j in range(2):
        bit[1] = j          # 1번째 원소
        for k in range(2):
            bit[2] = k      # 2번째 원소
            for l in range(2):
                bit[3] = l  # 3번째 원소
                print(bit)  # 생성된 부분집합 출력
```

### 부분집합의 원소의 합이 n인
```py
def f(i, k, t): # k개의 원소를 가진 배열 A, 부분집합 합이 t인 경우
    if i == k: # 모든 원소에 대해 결정하면
        ss = 0 # 부분집합 원소의 합
        for j in range(k):
            if bit[j]: # A[j]가 포함된 경우
                ss += A[j]
        if ss == t:
            for j in range(k):
                if bit[j]:  # A[j]가 포함된 경우
                    print(A[j], end = '')
            print()     # 부분집합 출력
    else:
        for j in range(1, -1, -1):
            bit[i] = j
            f(i+1, k, t)
        # bit[i] = 1
        # f(i+1, k, t)
        # bit[i] = 0
        # f(i+1, k, t)
        


N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0]*N # bit[i]는 A[i]가 부분집합에 포함되는지 표시
f(0, N)
```

### 가지치기 포함
```py
def f(i, k, s, t): # k개의 원소를 가진 배열 A, 부분집합 합이 t인 경우
    global cnt
    cnt += 1
    if s == t: # 모든 원소에 대해 결정하면
        for j in range(k):
            if bit[j]:  # A[j]가 포함된 경우
                print(A[j], end = '')
        print()     # 부분집합 출력
    elif i == k:    #모든 원소를 고려했으나 s!=t
        return
    elif s > t:
        return
    else:
        # for j in range(1, -1, -1):
        #     bit[i] = j
        #     f(i+1, k, s+A[i]*j t)
        bit[i] = 1
        f(i+1, k, s+A[i], t)
        bit[i] = 0
        f(i+1, k, s, t)
        
N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0]*N # bit[i]는 A[i]가 부분집합에 포함되는지 표시
f(0, N, 0, 10)
print(f'cnt :', cnt)
```

### 순열을 이용한 예제
```py
def f(i, k):
    global min_v
    global cnt
    cnt += 1
    if i==k:
        # print(*P)
        s = 0   # 선택한 원소의 합
        for j in range(k):  # j행에 대해
            s += arr[j][p[j]]   # j행에서 P[j] 열을 고른 경우의 합 구하기
        if min_v > s:
            min_v = s
    else:
        for j in range(i, k):    # P[i]자리에 올 원소 P[j]
            P[i], P[j] = P[j], P[i]     # P[i] <-> P[j]
            f(i+1, k)
            P[i], P[j] = P[j], P[i]     # 교환 전으로 복구

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
P = [i for i in range(N)]
min_v = 100
cnt = 0
f(0, N)
print(min_v)
```

### 가지치기 포함
```py
def f(i, k, s):     # i-1까지 선택한 원소의 합
    global min_v
    global cnt
    cnt += 1
    if i==k:
        if min_v > s:
            min_v = s
    elif s >= min_v:
        return
    else:
        for j in range(i, k):    # P[i]자리에 올 원소 P[j]
            P[i], P[j] = P[j], P[i]     # P[i] <-> P[j]
            f(i+1, k, s+arr[i][P[i]])
            P[i], P[j] = P[j], P[i]     # 교환 전으로 복구

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
P = [i for i in range(N)]
min_v = 100
cnt = 0
f(0, N, s)
print(min_v)
```

