def dfs(s, g):
    stack = []
    stack.append(s)

    while stack:
        node = stack.pop()

        if visited[node] == 0:
            visited[node] = 1
            for i in range(1, V + 1):
                if graph[node][i] == 1 and visited[i] == 0:
                    if i == g:
                        return 1
                    stack.append(i)
    return 0

T = int(input())

for tc in range(T):
    V, E = map(int, input().split())
    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for _ in range(E):
        i, j = map(int, input().split())
        graph[i][j] = 1

    S, G = map(int, input().split())
    result = dfs(S, G)
    print(f'#{tc+1} {result}')

