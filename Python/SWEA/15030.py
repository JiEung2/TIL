T = int(input())

for tc in range(T):
    s = list(input())
    stack = []

    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    print(f'#{tc+1} {len(stack)}')