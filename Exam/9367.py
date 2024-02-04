T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 1
    result = 0

    for i in range(N-1):
        if arr[i] < arr[i+1]:
            cnt += 1
        else:
            if result < cnt:
                result = cnt
            cnt = 1

    if result < cnt:
        result = cnt

    print(f'#{tc+1} {result}')