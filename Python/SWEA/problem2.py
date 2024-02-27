T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    pointX = 0
    pointY = 0
    sumV = 0
    before = 0
    while True:
        maxV = 0
        tmpX = pointX + M
        tmpY = pointY + M

        if tmpX >= N:
            tmpX = N
        if tmpY >= N:
            tmpY = N

        for i in range(pointX, tmpX):
            for j in range(pointY, tmpY):
                if maxV < board[i][j]:
                    maxV = board[i][j]
                    pointX = i
                    pointY = j
        if before == maxV:
            break
        before = maxV
        sumV += maxV

    print(f'#{tc+1} {sumV}')
