def dfs(L, sumV):
    global maxV
    if L == N:
        if maxV < sumV:
            maxV = sumV

    for i in range(N):
        if not visited[i] and board[L][i] != -1:
            visited[i] = 1
            dfs(L+1, sumV + board[L][i])
            visited[i] = 0

T = int(input())

for tc in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0

    visited = [0] * N

    dfs(0, 0)
    print(f'#{tc+1} {maxV}')