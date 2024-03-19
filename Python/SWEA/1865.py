def dfs(L, p):
    global maxV
    if p == 0:
        return

    if p < maxV:
        return

    if L == n:
        maxV = max(maxV, p)
        return

    for i in range(n):
        if visited[i] == 1: continue
        visited[i] = 1
        dfs(L + 1, p * arr[L][i] * 0.01)
        visited[i] = 0

T = int(input())

for tc in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    maxV = 0

    dfs(0, 1)
    print(f'#{tc+1}', end=' ')
    print("%.6f" % (maxV * 100))