# def perm(k, sumV):
#     global min_V
#     if k == N:
#         if min_V > sumV:
#             min_V = sumV
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             perm(k+1, sumV + numbers[k][i])
#             visited[i] = False
#
# min_V = 100
# N = 3
# numbers = [[2, 1, 2], [5, 8, 5], [7, 2, 2]]
# visited = [False] * N
# perm(0, 0)
# print(min_V)


T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))
    num_pizza = []
    oven = []
    for idx in range(M) :
      num_pizza.append([idx+1, pizzas[idx]]) #피자번호, 피자 넣기

    for put in range(N):
        oven.append(num_pizza[put])

    remain = num_pizza[N:]
    # print(remain)
    while len(oven) > 1 :
        idx, cheese = oven.pop(0)
        cheese //= 2
        if cheese != 0 :
            oven.append([idx, cheese])
        else :
            if remain:
                oven.append(remain.pop(0))
    print(f'#{tc} {oven.pop()[0]}')