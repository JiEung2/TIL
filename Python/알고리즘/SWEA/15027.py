T = int(input())

for tc in range(T):
    N = int(input()) // 10
    memo = [0] * (N+1)
    memo[0] = 1
    memo[1] = 1
    for i in range(2, N+1):
        memo[i] = memo[i-1] + memo[i-2] * 2

    print(f'#{tc+1} {memo[N]}')