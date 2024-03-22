T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    result_cnt = 0
    for i in range(N):
        for j in range(M):
            sumV = board[i][j]
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < N and 0 <= ny < M:
                    sumV += board[nx][ny]
            if result_cnt < sumV:
                result_cnt = sumV

    print(f'#{tc+1} {result_cnt}')