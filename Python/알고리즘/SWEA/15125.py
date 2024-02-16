def bfs(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append((x, y))
    visited[x][y] = 1
    while q:
        tx, ty = q.pop(0)
        if Map[tx][ty] == 3:
            return visited[tx][ty] - 2
        for d in range(4):
            nx = tx + dx[d]
            ny = ty + dy[d]
            if 0 <= nx < N and 0 <= ny < N and (Map[nx][ny] == 0 or Map[nx][ny] == 3) and visited[nx][ny] == 0:
                visited[nx][ny] = visited[tx][ty] + 1
                q.append((nx, ny))
    return 0


T = int(input())

for tc in range(T):
    N = int(input())
    Map = [list(map(int, input())) for _ in range(N)]

    sx = 0
    sy = 0
    for i in range(N):
        for j in range(N):
            if Map[i][j] == 2:
                sx = i
                sy = j

    print(f'#{tc+1} {bfs(sx, sy)}')