# 이전 코드랑 아예 똑같음
T = int(input())
for tc in range(T):
    n = int(input())
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    arr = [[0] * n for _ in range(n)]
    x = 0
    y = 0
    index = 0
    i = 1
    while i <= n*n:
        arr[x][y] = i
        nx = x + dx[index]
        ny = y + dy[index]

        if nx < 0 or nx >= n or ny < 0 or ny >= n or arr[nx][ny] > 0:
            index = (index + 1) % 4

        x = x + dx[index]
        y = y + dy[index]

        i += 1

    print(f'#{tc+1}')
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()