def prim(now):
    U = []
    D = [float('inf')] * V
    D[now] = 0

    while len(U) < V:
        minV = float('inf')
        for i in range(V):
            if i in U:
                continue
            if D[i] < minV:
                minV = D[i]
                now = i

        U.append(now)

        for i in range(V):
            if i in U: continue
            if G[now][i]:
                D[i] = min(D[i], G[now][i])

    return sum(D)

T = int(input())

for tc in range(T):
    result_cnt = float('inf')
    V, E = map(int, input().split())
    V += 1
    G = [[0] * V for _ in range(V)]
    for _ in range(E):
        v1, v2, w = map(int, input().split())
        G[v1][v2] = w
        G[v2][v1] = w

    print(f'#{tc+1} {prim(0)}')