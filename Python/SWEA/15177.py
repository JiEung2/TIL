def count_child(root):
    global cnt
    cnt += 1
    if len(TREE[root]):
        for i in range(len(TREE[root])):
            count_child(TREE[root][i])

T = int(input())

for tc in range(T):
    E, N = map(int, input().split())
    node_number = E+1
    TREE = [[] for _ in range((node_number+1))]
    lst = list(map(int, input().split()))

    for i in range(0, len(lst), 2):
        TREE[lst[i]].append(lst[i+1])

    cnt = 0
    count_child(N)

    print(f'#{tc+1} {cnt}')