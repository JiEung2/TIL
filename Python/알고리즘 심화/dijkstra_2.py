INF = int(1e6)


def dijk(now):
    U = []
    D = [INF] * V

    D[now] = 0
    while len(U) < V:
        minV = INF
        for i in range(V):
            if i in U: continue
            if D[i] < minV:
                minV = D[i]
                now = i

        U.append(now)

        for i in range(V):
            if i in U:
                continue
            if G[now][i]:
                D[i] = min(D[i], D[now] + G[now][i])

    print(U, D)


V, E = map(int, input().split())
G = [[0] * V for _ in range(V)]
for i in range(E):
    v1, v2, w = map(int, input().split())
    G[v1][v2] = w

dijk(0)
