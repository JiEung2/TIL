def recur(L, s, now):
    global minV
    if s > minV:
        return
    if L == N:
        tmp = s + Map[now][0]
        if tmp < minV:
            minV = tmp
        return

    for i in range(1, N):
        if not visited[i]:
            visited[i] = 1
            recur(L + 1, s + Map[now][i], i)
            visited[i] = 0

T = int(input())

for tc in range(T):
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]

    minV = float('inf')
    visited = [0] * N
    visited[0] = 1
    recur(1, 0, 0)

    print(f'#{tc+1} {minV}')
