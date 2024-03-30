from collections import deque
def bfs(start):
    q = deque()
    visited = [0] * 100
    visited[start] = 1
    q.append(start)

    while q:
        node = q.popleft()
        for i in range(100):
            if not visited[i] and G[node][i] == 1:
                visited[i] = visited[node] + 1
                q.append(i)

    maxV = 0
    max_index = -1
    for i in range(99, -1, -1):
        if maxV < visited[i]:
            maxV = visited[i]
            max_index = i

    return max_index

T = 10

for tc in range(T):
    G = [[0] * 100 for _ in range(100)]
    n, s = map(int, input().split())
    lst = list(map(int, input().split()))
    for i in range(0, n, 2):
        f = lst[i]
        t = lst[i+1]
        G[f-1][t-1] = 1

    print(f'#{tc+1} {bfs(s-1) + 1}')