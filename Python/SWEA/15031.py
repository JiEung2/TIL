def calc(v1, v2, op):
    if op == '+':
        return v1 + v2
    elif op == '-':
        return v1 - v2
    elif op == '*':
        return v1 * v2
    else:
        return v1 // v2

T = int(input())

for tc in range(T):
    lst = list(input().split())
    stack = []
    for c in lst:
        if c.isdigit():
            stack.append(int(c))
        elif c != '.':
            if len(stack) < 2:
                print(f'#{tc + 1} error')
                break
            a = stack.pop()
            b = stack.pop()
            stack.append(calc(b, a, c))
        else:
            result_cnt = stack.pop()
            if stack:
                print(f'#{tc + 1} error')
                break
            else:
                print(f'#{tc + 1} {result_cnt}')
