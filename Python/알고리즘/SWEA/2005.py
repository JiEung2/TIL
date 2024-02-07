def fibo(n):
    global memo
    for i in range(n):
        memo[i][0] = 1
        memo[i][-1] = 1
        for j in range(1, i):
            memo[i][j] = memo[i-1][j-1] + memo[i-1][j]

T = int(input())

for tc in range(T):
    n = int(input())
    memo = [[0] * (i + 1)for i in range(n)]

    fibo(n)
    print(f'#{tc+1}')
    for i in range(n):
        print(*memo[i])