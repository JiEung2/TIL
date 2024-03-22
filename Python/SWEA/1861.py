from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    cnt = 0

    while q:
        tx, ty = q.popleft()
        cnt += 1
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] - arr[tx][ty] == 1:
                q.append((nx, ny))
    return cnt

T = int(input())

for tc in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = 0
    max_number = 0

    for i in range(n):
        for j in range(n):
            cnt = bfs(i, j)
            if cnt > max_cnt:
                max_cnt = cnt
                max_number = arr[i][j]
            elif cnt == max_cnt and arr[i][j] < max_number:
                    max_number = arr[i][j]

    print(f'#{tc+1} {max_number} {max_cnt}')