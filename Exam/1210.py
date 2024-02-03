for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    target_col = 0
    for i in range(100):
        if arr[99][i] == 2:
            target_col = i
            break

    col = target_col
    row = 99

    while row > 0:
        if col > 0 and arr[row][col-1] == 1:
            while col > 0 and arr[row][col-1] == 1:
                col -= 1
        elif col < 99 and arr[row][col+1] == 1:
            while col < 99 and arr[row][col+1] == 1:
                col += 1
        row -= 1

    print(f'#{tc} {col}')