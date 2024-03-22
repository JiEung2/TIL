from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(visited):
    while q:
        tx, ty = q.popleft()
        for d in range(4):
            nx = tx + dx[d]
            ny = ty + dy[d]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and Map[nx][ny] == 'L':
                visited[nx][ny] = visited[tx][ty] + 1
                q.append((nx, ny))

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    Map = [input() for _ in range(N)]
    q = deque()
    visited = [[0] * M for _ in range(N)]

    result_cnt = 0
    for i in range(N):
        for j in range(M):
            if Map[i][j] == 'W':
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] == 'L':
                        q.append((nx, ny))
                        visited[nx][ny] = 1

    bfs(visited)

    for i in range(N):
        for j in range(M):
            result_cnt += visited[i][j]

    print(f'#{tc+1} {result_cnt}')