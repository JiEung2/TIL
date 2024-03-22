T = int(input())

for tc in range(T):
    s = [input() for _ in range(5)]
    result_cnt = ''

    for i in range(15):
        for j in range(5):
            if i >= len(s[j]):
                continue
            result_cnt += s[j][i]

    print(f'#{tc+1} {result_cnt}')