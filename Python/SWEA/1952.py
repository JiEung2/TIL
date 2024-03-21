def solve():
    d = [0] * m
    for i in range(1, m):
        tmp1 = d[i-1] + price[0] * month[i-1]
        tmp2 = d[i-1] + price[1]
        tmp3 = float('inf')
        if i >= 3:
            tmp3 = d[i-3] + price[2]
        tmp4 = float('inf')
        if i == 12:
            tmp4 = price[3]
        d[i] = min(tmp1, tmp2, tmp3, tmp4)

    return d[12]

T = int(input())

for tc in range(T):
    price = list(map(int, input().split()))
    month = list(map(int, input().split()))
    n = 4
    m = 13

    print(f'#{tc+1} {solve()}')
