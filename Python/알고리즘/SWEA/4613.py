def count_paint(p1, p2, WBR):
    sumV = 0
    for i in range(0, p1):
        sumV += WBR[i][1]
        sumV += WBR[i][2]
    for i in range(p1, p2):
        sumV += WBR[i][0]
        sumV += WBR[i][2]
    for i in range(p2, N):
        sumV += WBR[i][0]
        sumV += WBR[i][1]
    return sumV

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    flag = [input() for _ in range(N)]
    WBR = [[0]*3 for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if flag[i][j] == 'W':
                WBR[i][0] += 1
            elif flag[i][j] == 'B':
                WBR[i][1] += 1
            else:
                WBR[i][2] += 1
    minV = N*M
    for point1 in range(1, N-1):
        for point2 in range(point1+1, N):
            value = count_paint(point1, point2, WBR)
            if minV > value:
                minV = value

    print(f'#{tc+1} {minV}')