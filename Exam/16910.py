T = int(input())

for tc in range(T):
    n = int(input())
    result = 0
    for i in range(-n, n+1):
        for j in range(-n, n+1):
            if i**2 + j**2 <= n**2:
                result += 1

    print(f'#{tc+1} {result}')