def cal(a, b, index):
    if index == 0:
        return a + b
    if index == 1:
        return a - b
    if index == 2:
        return a * b
    else:
        return int(a / b)

def dfs(cnt, sumV):
    global max_value, min_value
    if cnt == n-1:
        max_value = max(sumV, max_value)
        min_value = min(sumV, min_value)
        return

    for i in range(4):
        if oper[i] > 0:
            oper[i] -= 1
            dfs(cnt + 1, cal(sumV, numbers[cnt+1], i))
            oper[i] += 1


T = int(input())

for tc in range(T):
    n = int(input())
    oper = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    min_value = float('inf')
    max_value = -float('inf')
    i = 0
    c = []

    dfs(0, numbers[0])
    print(f'#{tc+1} {max_value - min_value}')