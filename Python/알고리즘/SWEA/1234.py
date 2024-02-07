T = 10
for tc in range(T):
    N, number = input().split()

    stack = []
    for c in number:
        if stack:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
    print(f'#{tc+1}', ''.join(stack))