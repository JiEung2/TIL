def check(board):
    for i in range(len(board)):
        ch_row = [0] * 10
        ch_col = [0] * 10
        for j in range(len(board)):
            ch_row[board[i][j]] = 1
            ch_col[board[j][i]] = 1

            if i % 3 == 0 and j % 3 == 0:
                square_check = [0] * 10
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if square_check[board[x][y]]:
                            return 0
                        square_check[board[x][y]] = 1

        for j in range(1, 10):
            if ch_row[j] == 0:
                return 0
            if ch_col[j] == 0:
                return 0
    return 1

T = int(input())

for tc in range(T):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result_cnt = check(arr)
    print(f'{tc+1} {result_cnt}')