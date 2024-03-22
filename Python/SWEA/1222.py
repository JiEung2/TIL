for tc in range(10):
    N = int(input())
    stack = []
    result_cnt = []
    s = input()

    for c in s:
        if c.isdigit():
            result_cnt.append(c)
        else:
            if not stack:
                stack.append(c)
            else:
                result_cnt.append(stack.pop())
                stack.append(c)

    while stack:
        result_cnt.append(stack.pop())

    st = []
    for c in result_cnt:
        if c.isdigit():
            st.append(c)
        else:
            a = int(st.pop())
            b = int(st.pop())
            st.append(a+b)
    result_cnt = st.pop()
    print(f'#{tc+1} {result_cnt}')