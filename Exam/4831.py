T = int(input())

for tc in range(T):
    K, N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split())) + [N]

    M += 2
    now = 0
    cnt = 0
    result_cnt = 0

    for i in range(1, M):
        if arr[i] - arr[i-1] > K:
            result_cnt = 0
            break
        if now + K < arr[i]:
            cnt += 1
            now = arr[i-1]
            result_cnt = cnt
    print(f'#{tc+1} {result_cnt}')