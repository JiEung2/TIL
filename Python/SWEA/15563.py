def dfs(index, power, cnt):
    global result

    if cnt > result:
        return

    if index + power >= n:
        result = min(result, cnt)
        return

    for i in range(index + power, index, -1):
        if i >= n: continue
        dfs(i, arr[i], cnt + 1)

T = int(input())

for tc in range(T):
    result = float('inf')
    arr = list(map(int, input().split()))
    n = arr[0]

    dfs(1, arr[1], 0)
    print(f'#{tc+1} {result}')

