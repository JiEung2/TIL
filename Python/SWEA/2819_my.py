dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, string):
    if len(string) == 7:
        result_cnt.add(string)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, string + board[nx][ny])

T = int(input())

for tc in range(T):
    board = [list(input().split()) for _ in range(4)]

    result_cnt = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, "")

    print(f'#{tc+1} {len(result_cnt)}')