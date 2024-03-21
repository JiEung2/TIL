from collections import deque

def bfs(sx, sy):
    d = [[float('inf')] * n for _ in range(n)]
    d[sx][sy] = 0

    q = deque()
    q.append((sx, sy))

    while q:
        tx, ty = q.popleft()
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                tmpD = 1
                if arr[nx][ny] > arr[tx][ty]:
                    tmpD += arr[nx][ny] - arr[tx][ty]

                if d[nx][ny] > d[tx][ty] + tmpD:
                    d[nx][ny] = d[tx][ty] + tmpD
                    q.append((nx, ny))

    return d[n-1][n-1]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())

for tc in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{tc+1} {bfs(0, 0)}')