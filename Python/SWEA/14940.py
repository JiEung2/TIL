def check(s, N, M):
    for i in range(N):
        for j in range(N-M+1):
            k = j + M
            if s[i][j:k][::-1] == s[i][j:k]:
                return ''.join(s[i][j:k])

    for i in range(N):
        for j in range(N-M+1):
            tmp_lst2 = []
            for k in range(j, j+M):
                tmp_lst2.append(s[k][i])

            if tmp_lst2 == tmp_lst2[::-1]:
                return ''.join(tmp_lst2)


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    s = [list(input()) for _ in range(N)]
    result_cnt = check(s, N, M)

    print(f'#{tc+1} {result_cnt}')