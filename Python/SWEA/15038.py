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

def minSum(L, sumV):
    global minV
    if sumV >= minV:
        return
    if L == N-1:
        if sumV < minV:
            minV = sumV
        return
    for i in range(N):
        if check[i] == 0:
            check[i] = 1
            minSum(L+1, sumV + arr[L+1][i])
            check[i] = 0

T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    check = [0] * N
    # 2 1 2  012 021 102 120 201 210
    # 5 8 5
    # 7 2 2
    minV = 100
    for i in range(N):
        check[i] = 1
        minSum(0, arr[0][i])
        check[i] = 0

    print(f'#{tc+1} {minV}')

