T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    result = 'ON'
    for i in range(N):
        if not M & (1 << i):
            result = "OFF"
            break
    print(f'#{tc+1} {result}')