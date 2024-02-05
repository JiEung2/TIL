# T = int(input())
# number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#
# for _ in range(T):
#     tc, N = input().split()
#     count = [0] * 10
#     lst = input().split()
#
#     for num in lst:
#         count[number.index(num)] += 1
#
#     print(tc)
#     for i in range(len(count)):
#         for j in range(count[i]):
#             print(f'{number[i]}', end=' ')
#     print()


T = int(input())
for tc in range(1, T+1):
    tc_num, N = input().split()
    N = int(N)
    num_list = list(input().split())
    order = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5 , "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}
    for i in range(N):
        num_list[i] = order[num_list[i]]

    for i in range(N):
        minV = num_list[i]
        minP = i
        for j in range(i+1, N):
            if minV > num_list[j]:
                minV = num_list[j]
                minP = j
        num_list[i], num_list[minP] = num_list[minP], num_list[i]

    result = []

    for number in num_list:
        for key in order.keys():
            if order[key] == number:
                result.append(key)


    print(f'{tc_num}', *num_list)