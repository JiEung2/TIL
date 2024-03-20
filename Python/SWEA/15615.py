from collections import deque
def calc(number, index):
    if index == 0:
        return number + 1
    if index == 1:
        return number - 1
    if index == 2:
        return number * 2
    else:
        return number - 10

def bfs(n):

    visited[n] = 1
    q = deque()
    q.append(n)

    flag = 0
    while q:
        number = q.popleft()
        for i in range(4):
            tmp = calc(number, i)
            if 0 <= tmp < 1000001 and visited[tmp] == 0:
                visited[tmp] = visited[number] + 1
                q.append(tmp)
                if tmp == m:
                    flag = 1
                    break
        if flag:
            return

T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    visited = [0] * 1000001
    bfs(n)

    print(f'#{tc+1} {visited[m]-1}')