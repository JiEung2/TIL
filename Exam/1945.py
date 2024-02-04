T = int(input())

for tc in range(T):
    n = int(input())

    number = n
    result = [0] * 5
    while number > 1:
        if number % 11 == 0:
            result[4] += 1
            number //= 11
        if number % 7 == 0:
            result[3] += 1
            number //= 7
        if number % 5 == 0:
            result[2] += 1
            number //= 5
        if number % 3 == 0:
            result[1] += 1
            number //= 3
        if number % 2 == 0:
            result[0] += 1
            number //= 2

    print(f'#{tc+1}', *result)