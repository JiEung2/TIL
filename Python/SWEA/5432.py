T = int(input())

for tc in range(T):
    s = input()
    cnt = 0
    result_cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            if s[i-1] == '(':
                result_cnt += cnt
            else:
                result_cnt += 1
    print(f'#{tc+1} {result_cnt}')