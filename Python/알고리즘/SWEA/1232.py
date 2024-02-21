def search(node):
    if node:
        search(left[node])
        search(right[node])
        if Tree[node] == '+':
            Tree[node] = int(Tree[left[node]]) + int(Tree[right[node]])
        elif Tree[node] == '-':
            Tree[node] = int(Tree[left[node]]) - int(Tree[right[node]])
        elif Tree[node] == '*':
            Tree[node] = int(Tree[left[node]]) * int(Tree[right[node]])
        elif Tree[node] == '/':
            Tree[node] = int(Tree[left[node]]) // int(Tree[right[node]])
    return

T = 10

for tc in range(T):
    N = int(input())
    Tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for _ in range(N):
        lst = list(input().split())
        Tree[int(lst[0])] = lst[1]
        if len(lst) == 4:
            left[int(lst[0])] = (int(lst[2]))
            right[int(lst[0])] = (int(lst[3]))
    search(1)
    print(f'#{tc+1} {Tree[1]}')
