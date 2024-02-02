# 간단한 소인수 분해

T = int(input())

for tc in range(T):
    N = int(input())
    lst = [0] * 5
    while N > 1:
        if N % 11 == 0:
            N //= 11
            lst[4] += 1
        if N % 7 == 0:
            N //= 7
            lst[3] += 1
        if N % 5 == 0:
            N //= 5
            lst[2] += 1
        if N % 3 == 0:
            N //= 3
            lst[1] += 1
        if N % 2 == 0:
            N //= 2
            lst[0] += 1
    print(f'#{tc+1}', *lst)