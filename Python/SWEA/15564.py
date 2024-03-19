def dfs(L, sumV):
    global result
    if sumV > result:
        return

    if L == n:
        result = min(result, sumV)
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(L + 1, sumV + arr[L][i])
            visited[i] = 0

T = int(input())

for tc in range(T):
    result = float('inf')
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n

    dfs(0, 0)
    print(f'#{tc+1} {result}')