T = int(input())

for tc in range(T):
    n = int(input())

    number = n
    result_cnt = [0] * 5
    while number > 1:
        if number % 11 == 0:
            result_cnt[4] += 1
            number //= 11
        if number % 7 == 0:
            result_cnt[3] += 1
            number //= 7
        if number % 5 == 0:
            result_cnt[2] += 1
            number //= 5
        if number % 3 == 0:
            result_cnt[1] += 1
            number //= 3
        if number % 2 == 0:
            result_cnt[0] += 1
            number //= 2

    print(f'#{tc+1}', *result_cnt)