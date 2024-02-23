T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))
    carrots.sort()
    min_v = 1000

    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            if carrots[i] != carrots[i + 1] and carrots[j] != carrots[j + 1]:
                small = i + 1
                mid = j - i
                large = N - 1 - j

                if max(small, mid, large) <= N // 2:
                    if min_v > max(small, mid, large) - min(small, mid, large):
                        min_v = max(small, mid, large) - min(small, mid, large)

    if min_v == 1000:
        min_v = -1

    print(f'#{tc} {min_v}')