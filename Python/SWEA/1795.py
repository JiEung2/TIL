def dijkstra(now):
    d = [float('inf')] * (n+1)
    d[now] = 0
    U = []

    while len(U) < n:
        minV = float('inf')
        for i in range(n):
            if i in U: continue
            if minV > d[i]:
                minV = d[i]
                now = i

        U.append(now)

        for i in range(len(G[now])):
            if i in U: continue
            if G[now][i]:
                d[i] = min(d[i], d[now] + G[now][i])

    return d

T = int(input())

for tc in range(T):
    n, m, x = map(int, input().split())
    G = [[] * n for _ in range(n)]
    r = [[] * n for _ in range(n)]
    for _ in range(m):
        n1, n2, w = map(int, input().split())
        G[n1-1][n2-1] = w
        r[n2-1][n1-1] = w

    gD = dijkstra()

