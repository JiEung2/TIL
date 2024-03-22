T = int(input())

for tc in range(T):
    s = input()
    stack = []
    lst = ['(', ')', '{', '}']
    for ch in s:
        if ch in lst:
            if stack:
                if ch == lst[1] and stack[-1] == lst[0]:
                    stack.pop()
                elif ch == lst[3] and stack[-1] == lst[2]:
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
    result_cnt = 1
    if stack:
        result_cnt = 0
    print(f'#{tc+1} {result_cnt}')
