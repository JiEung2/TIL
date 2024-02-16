# def dfs(L, s):
#     global minLevel
#     if L >= minLevel:
#         return
#     elif s == D:
#         if L < minLevel:
#             minLevel = L
#     else:
#         for node in G[s]:
#             if check[node] == 0:
#                 check[node] = 1
#                 dfs(L+1, node)
#                 check[node] = 0
#
# T = int(input())
#
# for tc in range(T):
#     V, E = map(int, input().split())
#     G = [[] for i in range(V + 1)]
#     check = [0] * (V + 1)
#     minLevel = float('inf')
#     for _ in range(E):
#         node1, node2 = map(int, input().split())
#         G[node1].append(node2)
#         G[node2].append(node1)
#     S, D = map(int, input().split())
#     dfs(0, S)
#     if minLevel == float('inf'):
#         minLevel = 0
#     print(f'#{tc+1} {minLevel}')

def bfs(s, N, G):
    q = []
    visited = [0] * (N + 1)
    q.append(s)
    visited[s] = 1
    while q:
        t = q.pop(0)
        if t == G:
            return visited[t] - 1
        for i in adjl[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t]+1
    return 0


T = int(input())

for tc in range(T):
    V, E = map(int, input().split())
    adjl = [[] for i in range(V + 1)]
    minLevel = float('inf')
    for _ in range(E):
        node1, node2 = map(int, input().split())
        adjl[node1].append(node2)
        adjl[node2].append(node1)
    S, G = map(int, input().split())
    print(f'#{tc+1} {bfs(S, V, G)}')
