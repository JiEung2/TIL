T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    result_cnt = 'ON'
    for i in range(N):
        if not M & (1 << i):
            result_cnt = "OFF"
            break
    print(f'#{tc+1} {result_cnt}')