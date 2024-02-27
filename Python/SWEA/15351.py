dx = [1, 0]
dy = [0, 1]

def recur(x, y, s):
    global minV
    if s >= minV:
        return
    if x == N-1 and y == N-1:
        if minV > s:
            minV = s
        return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            recur(nx, ny, s + Map[nx][ny])

T = int(input())

for tc in range(T):
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]

    minV = float('inf')
    recur(0, 0, Map[0][0])

    print(f'#{tc+1} {minV}')