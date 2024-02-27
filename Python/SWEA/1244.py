# def recur(L, phase):
#     global maxV
#     if L == M * 2:
#         tmp = N
#         for i in range(0, M*2, 2):
#             i1 = change[i]
#             i2 = change[i+1]
#             tmp[i1], tmp[i2] = tmp[i2], tmp[i1]
#
#         number = int(''.join(tmp))
#         if maxV < number:
#             maxV = number
#
#     for i in range(len(N)):
#         if visited[i] < ((phase // 2)+1):
#             visited[i] += 1
#             change.append(i)
#             recur(L + 1, phase + 1)
#             visited[i] -= 1
#             change.pop()
#
# T = int(input())
#
# for tc in range(T):
#     N, M = input().split()
#     N = list(N)
#     M = int(M)
#     visited = [0] * len(N)
#     change = []
#     maxV = 0
#
#     recur(0, 1)
#     print(f'#{tc+1} {maxV}')


# def find_max(arr):
#     max = 0
#     index = 0
#     for i in range(len(arr)):
#         if arr[i] >= max:
#             max = arr[i]
#             index = i
#     return index
#
# T = int(input())
#
# for tc in range(T):
#     N, M = input().split()
#     M = int(M)
#     N = list(map(int, N))
#     i = 0
#     while M > 0 and i < len(N)-1:
#         max_index = find_max(N[i + 1: len(N)]) + (i+1)
#         if N[i] < N[max_index] and i < max_index:
#             N[i], N[max_index] = N[max_index], N[i]
#             M -= 1
#         i += 1
#
#     result = ''.join(map(str, N))
#     if M > 0 and M % 2 == 1:
#         N[-2], N[-1] = N[-1], N[-2]
#
#     print(f'#{tc+1} {result}')

def dfs(L):
    global result
    if L == N:
        result = max(result, int(''.join(map(str, numbers))))
        return
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            now = int(''.join(map(str, numbers)))
            if (L, now) not in visited:
                dfs(L+1)
                visited.append((L, now))

            numbers[i], numbers[j] = numbers[j], numbers[i]

T = int(input())

for tc in range(T):
    numbers, N = input().split()
    N = int(N)
    numbers = list(map(int, numbers))
    visited = []
    result = 0
    dfs(0)
    print(f'#{tc+1} {result}')