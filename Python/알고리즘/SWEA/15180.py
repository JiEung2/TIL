def sum_parent(child):
    if child == 0:
        return 0
    return Tree[child] + sum_parent(child // 2)

def enqueue(number):
    global last
    last += 1

    Tree[last] = number
    c = last
    p = last // 2
    while p:
        if Tree[c] < Tree[p]:
            Tree[c], Tree[p] = Tree[p], Tree[c]
            c = p
            p = c//2
        else:
            break

T = int(input())

for tc in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    Tree = [0] * (N + 1)
    last = 0

    for i in lst:
        enqueue(i)

    result = sum_parent(N//2)
    print(f'#{tc+1} {result}')