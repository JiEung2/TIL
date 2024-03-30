def dfs(L, now, sumV):
    global result
    if sumV > result:
        return

    if L == n:
        tmp = sumV + arr[now][0]
        result = min(result, tmp)

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(L + 1, i, sumV + arr[now][i])
            visited[i] = 0

T = int(input())

for tc in range(T):
    result = float('inf')
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    visited[0] = 1
    dfs(1, 0, 0)

    print(f'#{tc+1} {result}')