def dfs(index, sumV):
    global result
    if sumV > result:
        return

    if sumV + sum(h[index:]) < B:
        return

    if sumV >= B:
        if sumV < result:
            result = sumV
        return

    for i in range(index, N):
        if not visited[i]:
            visited[i] = 1
            dfs(i, sumV + h[i])
            visited[i] = 0

T = int(input())

for tc in range(T):
    N, B = map(int, input().split())
    h = list(map(int, input().split()))
    result = float('inf')
    visited = [0] * N

    dfs(0, 0)
    print(f'#{tc+1} {result - B}')