def max(a, b):
    if a > b:
        return a
    return b

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    maxV = 0
    sum_right = 0
    sum_left = 0
    tmp_max = 0
    for i in range(100):
        sum_row = 0
        sum_col = 0

        for j in range(100):
            sum_row += arr[i][j]
            sum_col += arr[j][i]

        sum_right += arr[i][i]
        sum_left += arr[i][100-1-i]
        tmp_max = max(tmp_max,max(sum_row, sum_col))

    tmp_max = max(tmp_max, max(sum_right,sum_left))

    print(f'#{tc} {tmp_max}')
