T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    w.sort()
    t.sort()
    wi = len(w) - 1
    ti = len(t) - 1
    result_cnt = 0

    while wi >= 0 and ti >= 0:
        if w[wi] <= t[ti]:
            result_cnt += w[wi]
            ti -= 1
        wi -= 1

    print(f'#{tc+1} {result_cnt}')