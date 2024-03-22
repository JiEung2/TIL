def find_min(arr):
    minV = arr[0]
    minIndex = 0
    for i in range(1, len(arr)):
        if minV > arr[i]:
            minV = arr[i]
            minIndex = i

    return minIndex


def find_max(arr):
    maxV = arr[0]
    maxIndex = 0
    for i in range(1, len(arr)):
        if maxV < arr[i]:
            maxV = arr[i]
            maxIndex = i

    return maxIndex


for tc in range(10):
    N = int(input())
    arr = list(map(int, input().split()))

    max_index = 0
    min_index = 0
    result_cnt = 0
    for i in range(N):
        max_index = find_max(arr)
        min_index = find_min(arr)

        if arr[max_index] - arr[min_index] == 1:
            break

        arr[max_index] -= 1
        arr[min_index] += 1

    result_cnt = arr[find_max(arr)] - arr[find_min(arr)]
    print(f'#{tc+1} {result_cnt}')
