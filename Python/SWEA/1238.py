from collections import deque

def bfs(s):
    q = deque()
    visited[s] = 1
    q.append(s)

    while q:
        tmp = q.popleft()

        for i in range(len(link[tmp])):
            if not visited[link[tmp][i]]:
                visited[link[tmp][i]] = visited[tmp] + 1
                q.append(link[tmp][i])

T = 10

for tc in range(T):
    n, s = map(int, input().split())
    lst = list(map(int, input().split()))
    link = [[] for _ in range(101)]

    for i in range(0, n, 2):
        link[lst[i]].append(lst[i+1])
    visited = [0] * 101

    bfs(s)
    result = 0
    max = 0
    for i in range(100, -1, -1):
        if max < visited[i]:
            max = visited[i]
            result = i

    print(f'#{tc+1} {result}')