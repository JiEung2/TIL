T = int(input())

for tc in range(T):
    N = int(input())
    lst = list(input())
    result_cnt = 0
    cnt = 0
    for i in range(N):
        if int(lst[i]) == 1:
            cnt += 1
        else:
            if result_cnt < cnt:
                result_cnt = cnt
            cnt = 0
    if result_cnt < cnt:
        result_cnt = cnt

    print(f'#{tc+1} {result_cnt}')
