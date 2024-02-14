def perm(k, sumV):
    global min_V
    if k == N:
        if min_V > sumV:
            min_V = sumV
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            perm(k+1, sumV + numbers[k][i])
            visited[i] = False

min_V = 100
N = 3
numbers = [[2, 1, 2], [5, 8, 5], [7, 2, 2]]
visited = [False] * N
perm(0, 0)
print(min_V)
