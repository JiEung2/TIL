T = int(input())

for tc in range(T):
    N = int(input())
    busStop = [0] * 5001
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            busStop[i] += 1

    P = int(input())
    lst = [int(input()) for _ in range(P)]
    print(f'#{tc+1}', end=' ')
    for i in range(P):
        print(f'{busStop[lst[i]]}', end=' ')
    print()