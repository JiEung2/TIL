T = int(input())

for tc in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, 0, -1, 0, 2, 0, -2, 0]
    dy = [0, 1, 0, -1, 0, 2, 0, -2]

    result_cnt = 0

    for i in range(N):
        for j in range(N):
            tmp_sum = board[i][j]
            for d in range(8):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    tmp_sum += board[nx][ny]
            if tmp_sum > result_cnt:
                result_cnt = tmp_sum

    print(f'#{tc+1} {result_cnt}')