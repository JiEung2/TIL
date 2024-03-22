T = int(input())

for tc in range(T):
    N = int(input())
    Map = [list(map(int, input())) for _ in range(N)]
    check = [[0]*N for _ in range(N)]

    sx = 0
    sy = 0

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    for i in range(N):
        for j in range(N):
            if Map[i][j] == 2:
                sx = i
                sy = j

    stack = [(sx, sy)]
    check[sx][sy] = 1

    result_cnt = 0
    while stack:
        x, y = stack.pop()
        check[x][y] = 1
        if Map[x][y] == 3:
            result_cnt = 1
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and (Map[nx][ny] == 0 or Map[nx][ny] == 3) and check[nx][ny] == 0:
                stack.append((nx, ny))

    print(f'#{tc+1} {result_cnt}')