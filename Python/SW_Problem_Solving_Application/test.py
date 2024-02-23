# import sys
# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")
#
# a, b = map(int, input().split())
#
# print(a + b)
# print(a * b)

# def code(a, b):
#     return a ^ b
#
# N = int(input())
# key = 1004
# result = code(N, key)
# print(result)
#
# print(code(result, key))

# n = 1
# for i in range(5):
#     print(bin(n), n)
#     n = n << 1


# print(~10)

# T = int(input())
#
# for tc in range(T):
#     N, M = map(int, input().split())
#     result = 'ON'
#     for i in range(N):
#         if not M & (1<<i):
#             result = "OFF"
#             break
#     print(f'#{tc+1} {result}')

n = 0.1
print(f'{n:.20f}')