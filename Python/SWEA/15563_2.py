def dfs(now, cnt, e):
    global result

    if cnt >= result:
        return

    if now == f:
        result = min(result, cnt)
        return

    if e == 0:
        return
    dfs(now + 1, cnt, e-1)
    dfs(now + 1, cnt + 1, busStop[now + 1])

T = int(input())

for tc in range(T):
    result = float('inf')
    busStop = list(map(int, input().split())) + [0]
    f = busStop[0]

    dfs(1, 0, busStop[1])
    print(f'#{tc+1} {result}')


