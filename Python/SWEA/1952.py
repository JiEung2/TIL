def dfs(month, sum_cost):
    global ans

    # 기저조건
    # 1. 12월까지 다 봤네? 종료

    if month > 12:
        # 최소 비용
        ans = min(ans, sum_cost)
        return

    # 2. 이미 최소값을 넘어갔네? 종료
    if sum_cost > ans:
        return

    # 모두 1일권으로 구매
    dfs(month + 1, sum_cost + (days[month] * cost[0]))

    # 1달권 구매
    dfs(month + 1, sum_cost + cost[1])

    # 3달권 구매
    dfs(month + 3, sum_cost + cost[2])

    # 1년권 구매
    dfs(month + 12, sum_cost + cost[3])

# def solve():
#     d = [0] * m
#     for i in range(1, m):
#         tmp1 = d[i-1] + price[0] * month[i-1]
#         tmp2 = d[i-1] + price[1]
#         tmp3 = float('inf')
#         if i >= 3:
#             tmp3 = d[i-3] + price[2]
#         tmp4 = float('inf')
#         if i == 12:
#             tmp4 = price[3]
#         d[i] = min(tmp1, tmp2, tmp3, tmp4)
#
#     return d[12]

T = int(input())

for tc in range(T):
    cost = list(map(int, input().split()))
    days = [0] + list(map(int, input().split()))

    ans = int(1e9)
    dfs(1, 0)
    print(ans)

    # price = list(map(int, input().split()))
    # month = list(map(int, input().split()))
    # n = 4
    # m = 13
    #
    # print(f'#{tc+1} {solve()}')
