T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    result_cnt = 0
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            cnt += 1
        else:
            if result_cnt < cnt:
                result_cnt = cnt
            cnt = 1

    if result_cnt < cnt:
        result_cnt = cnt

    print(f'#{tc+1} {result_cnt}')