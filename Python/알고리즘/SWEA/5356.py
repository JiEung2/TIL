T = int(input())

for tc in range(T):
    s = [input() for _ in range(5)]
    result = ''

    for i in range(15):
        for j in range(5):
            if i >= len(s[j]):
                continue
            result += s[j][i]

    print(f'#{tc+1} {result}')