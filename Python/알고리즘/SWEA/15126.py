from collections import deque

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))

    index = 0
    dq = deque()
    while index < N:
        dq.append((index, C[index]))
        index += 1

    index -= 1
    while len(dq) > 1:
        i, cheese = dq.popleft()
        cheese //= 2
        if cheese != 0:
            dq.append((i, cheese))
        else:
            index += 1
            if index < M:
                dq.append((index, C[index]))

    print(f'#{tc + 1} {dq.pop()[0] + 1}')
