for tc in range(1, 11) :
    input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    #각 행의 합을 구한다
    maxV = 0
    for row in range(100) :
        sumR = 0
        for col in range(100) :
            sumR += arr[row][col]
        if maxV <= sumR :
            maxV = sumR

    #각 열의 합을 구한다
    for col in range(100) :
        sumC = 0
        for row in range(100) :
            sumC += arr[row][col]
        if maxV <= sumC :
            maxV = sumC

    #우하향 대각선의 합을 구한다
    # 좌하향 대각선의 합을 구한다
    sumRCROSS = 0
    sumLCROSS = 0
    for row in range(100) :
        sumRCROSS += arr[row][row]
        sumLCROSS += arr[row][99-row]
    if maxV <= sumRCROSS :
        maxV = sumRCROSS
    if maxV <= sumLCROSS :
        maxV = sumLCROSS

    print(f'#{tc} {maxV}')