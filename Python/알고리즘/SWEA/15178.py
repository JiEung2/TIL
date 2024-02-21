def inOrder(node):
    global n
    if node > N:
        return

    inOrder(node * 2)
    TREE[node] = n
    n += 1
    inOrder(node * 2 + 1)

T = int(input())
for tc in range(T):
    N = int(input())
    TREE = [0] * (N+1)
    n = 1
    inOrder(1)

    print(f'#{tc+1} {TREE[1]} {TREE[N//2]}')