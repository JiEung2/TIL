T = int(input())

for tc in range(T):
    N = int(input())
    cnt = 0
    for i in range(-N, N+1):
        for j in range(-N, N+1):
            if i*i + j*j <= N*N:
                cnt += 1

    print(f'#{tc+1} {cnt}')