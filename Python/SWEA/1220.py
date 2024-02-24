T = 10

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        flag = False
        for j in range(N):
            if arr[j][i] == 1:
                flag = True
            if arr[j][i] == 2:
                if flag:
                    cnt += 1
                    flag = False

    print(f'#{tc+1} {cnt}')