def dc(node):
    if node > N:
        return 0
    if node > N // 2:
        return TREE[node]
    a = dc(node * 2)
    b = dc(node * 2 + 1)
    TREE[node] = a + b
    return TREE[node]

T = int(input())

for tc in range(T):
    N, M, L = map(int, input().split())
    TREE = [0] * (N + 1)
    for _ in range(M):
        node, number = map(int, input().split())
        TREE[node] = number

    result = dc(L)
    print(f'#{tc+1} {result}')