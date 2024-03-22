T = int(input())

for tc in range(T):
    n = int(input())
    result_cnt = 0
    for i in range(-n, n+1):
        for j in range(-n, n+1):
            if i**2 + j**2 <= n**2:
                result_cnt += 1

    print(f'#{tc+1} {result_cnt}')