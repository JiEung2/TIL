# def f(i, k):
#     if i == k:
#         for j in range(k):
#             if bit[j]:
#                 print(arr[j], end='')
#         print()
#     else:
#         # for k in range(2):
#         #     bit[i] = j
#         #     f(i+1, k)
#         bit[i] = 1
#         f(i+1, k)
#         bit[i] = 0
#         f(i+1, k)
#
#
# N = 4
# arr = [1, 2, 3, 4]
# bit = [0] * N
# f(0, N)


# N = 3
# result = [-1] * N
#
#
# # c 배열에 후보를 만들어서 갯수를 return
# def construct_candidates(k, c):
#     c[0] = 0
#     c[1] = 1
#     c[2] = 2
#     # c[0] = 0 + v
#     # c[1] = 1 + v
#     # c[2] = 2 + v
#     return 3
#
# def process_solution():
#     print(result)
#
# def recur_g(k):
#     if k == N:
#         process_solution()
#         return
#
#     c = [-1] * 100
#     nC = construct_candidates(k, c)
#     for i in range(nC):
#         result[k] = c[i]
#         recur_g(k + 1)
#
# recur_g(0)


# N = 3
# result = [-1]*N
# numbers= [23,42,15]
# #c 배열에 후보를 만들어서 갯수를 return
# def construct_candidates(k,c): #나부터 만들어서 3개/내가v일때 나를 기준으로 하려면 +v
#     c[0]=0
#     c[1]=1
#     return 2
#
# def process_solution():
#     print(result)
#     for i in range(N):
#         if result[i]:
#             print(numbers[i], end=' ')
#     print()
#
#
# def recur_g(k):     # k는 인덱스 번호
#     if k == N:  # N 전까진 다 봐야함, N-1째의 값이 N에서 나오기 때문
#         process_solution()
#         return
#     c = [-1]*100
#     nC = construct_candidates(k, c)  # k의 후보 만들어줘
#     for i in range(nC):    # 반복문은 옆의 가지들
#         result[k] = c[i]
#         recur_g(k+1)    # 호출하는 아래 덱스
#
# recur_g(0)

N = 10
result_cnt = [-1] * N
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def subSum(k, curS):
    if curS > 10:
        return
    if k == N:
        if curS == 10:
            print(result_cnt)
            for i in range(N):
                if result_cnt[i]:
                    print(numbers[i], end='')
                print()
        return

    for d in [0, 1]:
        result_cnt[k] = d
        if d == 0:
            subSum(k + 1, curS)
        else:
            subSum(k + 1, curS + numbers[k])


subSum(0, 0)
