def calc(a, b, op):
    if op == '+':
        return a + b
    else:
        return a * b

T = 10
for tc in range(T):
    N = int(input())
    s = input()
    result_cnt = ''
    stack = []

    prio = {'+': 1, '*': 2}

    for c in s:
        if c.isdigit():
            result_cnt += c
        else:
            if stack and prio[stack[-1]] < prio[c]:
                    stack.append(c)
            else:
                while stack and prio[stack[-1]] >= prio[c]:
                    result_cnt += stack.pop()
                stack.append(c)

    while stack:
        result_cnt += stack.pop()

    for c in result_cnt:
        if c.isdigit():
            stack.append(int(c))
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(calc(a, b, c))

    print(f'#{tc+1} {stack.pop()}')