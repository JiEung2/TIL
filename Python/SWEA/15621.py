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

    return D[N]

INF = float('inf')
T = int(input())

for tc in range(T):
    N, E = map(int, input().split())
    V = N + 1
    G = [[0] * V for _ in range(V)]

    for i in range(E):
        s, e, w = map(int, input().split())
        G[s][e] = w

    print(f'#{tc+1} {dijk(0)}')

