def dfs(k, sumV):
    global result
    if sumV > result:
        return

    if sumV + sum(people[k:]) < b:
        return

    if k == n:
        if sumV >= b:
            result = min(result, sumV)
        return

    visited[k] = 0
    dfs(k + 1, sumV)
    visited[k] = 1
    dfs(k + 1, sumV + people[k])
    return

T = int(input())

for tc in range(T):
    result = float('inf')
    n, b = map(int, input().split())
    people = list(map(int, input().split()))
    visited = [0] * n

    dfs(0, 0)
    print(f'#{tc+1} {result - b}')