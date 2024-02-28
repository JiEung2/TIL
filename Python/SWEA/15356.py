T = int(input())

for tc in range(T):
    N = int(input())
    work = []
    for _ in range(N):
        s, e = map(int, input().split())
        work.append((s, e))

    work.sort(key=lambda x: x[1])
    now = 0
    result = 0
    for i in range(len(work)):
        if work[i][0] >= now:
            result += 1
            now = work[i][1]

    print(f'#{tc+1} {result}')
