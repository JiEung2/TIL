'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

INF = int(1e6)
def prim(now):
    U = []
    D = [INF] * V
    D[now] = 0

    while len(U) < V:
        # D에 저장된 것 중 제일 작은 값인 vertex를 고른다.
        # 단, 아직 안가본 것 중
        minV = INF
        for i in range(V):
            if i in U: continue
            if D[i] < minV:
                minV = D[i]
                now = i

        U.append(now)

        # now와 연결된 vertex들의 값을 최소로 update
        for i in range(V):
            if i in U: continue
            if G[now][i]:
                D[i] = min(D[i], G[now][i])

        print(U, D)

V, E = map(int, input().split())
G = [[0]*V for _ in range(V)]

for i in range(E):
    v1, v2, w = map(int, input().split())
    G[v1][v2] = w
    G[v2][v1] = w
# print(G)

prim(0)