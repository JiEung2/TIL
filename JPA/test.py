def findMaxIndex(arr):
    for i in range(len(arr)-1, 0, -1):
        if arr[i] >= 1:
            return i

def findMinIndex(arr):
    for i in range(1, len(arr)):
        if arr[i] >= 1:
            return i

for tc in range(10):
    N = int(input())
    box = list(map(int, input().split()))
    count = [0] * 101

    for number in box:
        count[number] += 1
        
    for _ in range(N):
        maxI = findMaxIndex(count)
        minI = findMinIndex(count)

        if maxI - minI <= 1:
            break
        count[maxI] -= 1
        count[maxI - 1] += 1
        count[minI] -= 1
        count[minI + 1] += 1
    
    result_max = findMaxIndex(count)
    result_min = findMinIndex(count)
    print(f'#{tc+1} {result_max - result_min}')