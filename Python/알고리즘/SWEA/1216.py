def check(s, n, m):
    for i in range(n):
        for j in range(n - m + 1):
            k = j + m
            if s[i][j:k][::-1] == s[i][j:k]:
                return m

    for i in range(n):
        for j in range(n - m + 1):
            tmp_lst2 = ''
            for k in range(j, j + m):
                tmp_lst2 += s[k][i]

            if tmp_lst2 == tmp_lst2[::-1]:
                return m
    return 0


for tc in range(10):
    N = 100
    input()
    s = [input() for _ in range(N)]

    result = 0
    for i in range(N, 0, -1):
        result = check(s, N, i)
        if result != 0:
            break

    print(f'#{tc+1} {result}')