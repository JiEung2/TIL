def recur(depth, sumV, i):
    global cnt
    if depth == N:
        if sumV == K:
            cnt += 1
        return
    for i in range(i, 13):
            recur(depth + 1, sumV + i, i+1)


T = int(input())

for tc in range(T):
    cnt = 0
    N, K = map(int, input().split())
    recur(0, 0, 1)

    print(f'#{tc+1} {cnt}')
