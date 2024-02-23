for tc in range(10):
    N = int(input())
    stack = []
    result = []
    s = input()

    for c in s:
        if c.isdigit():
            result.append(c)
        else:
            if not stack:
                stack.append(c)
            else:
                result.append(stack.pop())
                stack.append(c)

    while stack:
        result.append(stack.pop())

    st = []
    for c in result:
        if c.isdigit():
            st.append(c)
        else:
            a = int(st.pop())
            b = int(st.pop())
            st.append(a+b)
    result = st.pop()
    print(f'#{tc+1} {result}')