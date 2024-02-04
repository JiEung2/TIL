T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    result = 0

    for i in range(N):
        for j in range(M):
            sumV = board[i][j]
            power = board[i][j]
            for d in range(4):
                now = 0
                nx = i + dx[d]
                ny = j + dy[d]
                while now < power:
                    if 0 <= nx < N and 0 <= ny < M:
                        sumV += board[nx][ny]
                    else:
                        break
                    now += 1
                    nx += dx[d]
                    ny += dy[d]
            if result < sumV:
                result = sumV

    print(f'#{tc+1} {result}')

