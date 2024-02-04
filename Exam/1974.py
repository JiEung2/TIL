def check_sudoku(arr):

    for i in range(9):
        row = [0] * 10
        col = [0] * 10
        for j in range(9):
            if row[arr[i][j]] or col[arr[j][i]]:
                return 0
            row[arr[i][j]] = 1
            col[arr[j][i]] = 1

            if i % 3 == 0 and j % 3 == 0:
                square = [0] * 10
                for k in range(3):
                    for z in range(3):
                        if square[arr[i+k][j+z]]:
                            return 0
                        square[arr[i+k][j+z]] = 1

    return 1


T = int(input())

for tc in range(T):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    result = check_sudoku(sudoku)

    print(f'#{tc+1} {result}')