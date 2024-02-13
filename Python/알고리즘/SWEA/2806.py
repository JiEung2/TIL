def check(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[x] - board[i]) == x - i:
            return False
    return True

def dfs(x):
    global result

    if x == N:
        result += 1
        return

    for i in range(N):
        board[x] = i
        if check(x):
            dfs(x+1)

T = int(input())

for tc in range(T):
    N = int(input())

    board = [0] * N
    result = 0

    dfs(0)

    print(f'#{tc+1} {result}')
