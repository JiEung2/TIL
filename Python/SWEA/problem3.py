def work1(start, finish):
    tmp = start + finish
    if tmp >= N:
        tmp = N
    for i in range(start, tmp):
        rocks[i] = abs(rocks[i] - 1)

def work2(start, finish):
    rock = rocks[start]
    for i in range(start+1, start+finish):
        rocks[i] = rock

def work3(start, finish):
    point = 1
    while point <= finish:
        if start + point >= N or start - point < 0:
            break
        if rocks[start + point] == rocks[start - point]:
            rocks[start + point] = abs(rocks[start + point] - 1)
            rocks[start - point] = abs(rocks[start - point] - 1)
        point += 1

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    rocks = list(map(int, input().split()))

    for _ in range(M):
        i, j, w = map(int, input().split())
        if w == 1:
            work1(i-1, j)
        elif w == 2:
            work2(i-1, j)
        else:
            work3(i-1, j)

    print(f'#{tc+1}', end=' ')
    for i in range(N):
        print(rocks[i], end=' ')
    print()