T = int(input())

for tc in range(T):
    N = float(input())
    s = ''
    cnt = 0
    while N > 0:
        if cnt > 12:
            s = 'overflow'
            break
        tmp = N * 2
        s += str(tmp)[0]
        N = tmp - int(tmp)
        cnt += 1

    print(f'#{tc+1} {s}')