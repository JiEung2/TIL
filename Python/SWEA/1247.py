def dfs(L, now, sumV):
    global result
    # print(sumV)

    if sumV > result:
        return

    if L == n:
        tmp = abs(lst[now][0] - lst[1][0]) + abs(lst[now][1] - lst[1][1])
        result = min(result, sumV + tmp)
        return

    for i in range(2, n+2):
        if not visited[i]:
            visited[i] = 1
            dfs(L + 1, i, sumV + abs(lst[now][0] - lst[i][0]) + abs(lst[now][1] - lst[i][1]))
            visited[i] = 0

T = int(input())

for tc in range(T):
    result = float('inf')
    n = int(input())
    arr = list(map(int, input().split()))
    lst = []

    visited = [0] * (n+2)
    for i in range(0, len(arr), 2):
        lst.append([arr[i], arr[i+1]])

    dfs(0, 0, 0)
    print(f'#{tc+1} {result}')