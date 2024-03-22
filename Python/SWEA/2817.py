def dfs(L, k):
    global result_cnt
    if k == K:
        result += 1
        return

    if k > K:
        return

    for i in range(L, n):
        dfs(i + 1, k + arr[i])


T = int(input())

for tc in range(T):
    n, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result_cnt = 0

    dfs(0, 0)
    print(f'#{tc+1} {result_cnt}')
