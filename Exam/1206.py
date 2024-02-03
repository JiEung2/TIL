for tc in range(10):
    N = int(input())
    arr = list(map(int, input().split()))
    dx = [-2, -1, 1, 2]
    result = 0
    for i in range(2, N-2):
        if arr[i] > arr[i-1] and arr[i] > arr[i-2] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            maxV = 0
            for j in dx:
                if maxV < arr[i+j]:
                    maxV = arr[i+j]

            result += arr[i] - maxV
    print(f'#{tc+1} {result}')