T = int(input())

for tc in range(T):
    s = input()
    result_cnt = 0

    if s == s[::-1]:
        result_cnt = 1

    print(f'#{tc+1} {result_cnt}')