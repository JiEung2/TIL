T = int(input())

for tc in range(T):
    s = input()
    # 이렇게 해볼까
    d = {'d': 'b', 'b': 'd', 'p': 'q', 'q': 'p'}
    result_cnt = ''
    for i in range(len(s)-1, -1, -1):
        result_cnt += d[s[i]]

    print(f'#{tc+1} {result_cnt}')