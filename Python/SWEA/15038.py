def minSum(k, s):
    global minV

    if k == N:
        if minV > s:
            minV = s
    elif s >= minV:
        return
    else:
        for i in range(k, N):
            P[k], P[i] = P[i], P[k]
            minSum(k+1, s+arr[k][P[k]])
            P[k], P[i] = P[i], P[k]

T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = [i for i in range(N)]
    minV = 100
    minSum(0, 0)
    print(f'#{tc+1} {minV}')