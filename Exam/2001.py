T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    result_cnt = 0
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N-M+1):
        for j in range(N-M+1):
            sumV = 0
            for k in range(M):
                for z in range(M):
                    sumV += arr[i+k][j+z]
            if result_cnt < sumV:
                result_cnt = sumV
    print(f'#{tc+1} {result_cnt}')