T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    result = 0
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            cnt += 1
        else:
            if result < cnt:
                result = cnt
            cnt = 1

    if result < cnt:
        result = cnt

    print(f'#{tc+1} {result}')