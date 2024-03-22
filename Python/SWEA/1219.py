def dfs(v):
    stack = [v]
    while stack:
        tmp = stack.pop()

        if not visited[tmp]:
            visited[tmp] = True
            for node in G[tmp]:
                if not visited[node]:
                    if node == d:
                        return 1
                    stack.append(node)
    return 0


for _ in range(10):
    tc, N = map(int, input().split())
    G = [[] for _ in range(100)]
    lst = list(map(int, input().split()))
    visited = [False] * 100

    for i in range(0, N*2, 2):
        G[lst[i]].append(lst[i+1])

    d = 99
    result_cnt = dfs(0)
    print(f'#{tc} {result_cnt}')