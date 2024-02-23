from collections import deque

d = [[], [[1, 0], [-1, 0], [0, 1], [0, -1]], [[-1, 0], [1, 0]]
         , [[0, 1], [0, -1]], [[-1, 0], [0, 1]], [[1, 0], [0, 1]],
         [[1, 0], [0, -1]], [[-1, 0], [0, -1]]]

def checkCanGo(x, y, cx, cy):
    if Map[cx][cy] == 0:
        return False
    else:
        index = Map[cx][cy]
        for i in range(len(d[index])):
            dx, dy = d[index][i]
            nx = cx + dx
            ny = cy + dy
            if nx == x and ny == y:
                return True
    return False

def bfs(sx, sy, L):
    global cnt
    q = deque()
    q.append((sx, sy))
    visited = [[0] * M for _ in range(N)]
    visited[sx][sy] = 1
    while q:
        x, y = q.popleft()
        cnt += 1
        index = Map[x][y]
        for i in range(len(d[index])):
            dx, dy = d[index][i]
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and checkCanGo(x, y, nx, ny) and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                if visited[nx][ny] > L:
                    break
                q.append((nx, ny))

T = int(input())

for tc in range(T):
    N, M, R, C, L = map(int, input().split())
    Map = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    bfs(R, C, L)
    print(f'#{tc+1} {cnt}')
