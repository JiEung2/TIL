def inOrder(root):
    if len(TREE[root]) >= 1:
        inOrder(TREE[root][0])
    print(d[root], end='')
    if len(TREE[root]) >= 2:
        inOrder(TREE[root][1])

T = 10

for tc in range(T):
    N = int(input())
    d = {}
    TREE = [[] for _ in range(N+1)]

    for _ in range(N):
        lst = list(input().split())
        node = int(lst[0])
        ch = lst[1]
        d[node] = ch
        if len(lst) > 2:
            for i in range(2, len(lst)):
                TREE[node].append(int(lst[i]))

    print(f'#{tc+1}', end=' ')
    inOrder(1)
    print()