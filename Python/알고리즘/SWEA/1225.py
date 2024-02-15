# T = 10
# 
# for _ in range(T):
#     tc = int(input())
#     arr = list(map(int, input().split()))
#     i = 1
#     index = 0
#     while True:
#         if i == 6:
#             i = 1
#         ni = index % 8
#         arr[ni] -= i
#         if arr[ni] <= 0:
#             arr[ni] = 0
#             break
#         i += 1
#         index += 1
# 
#     print(f'#{tc}', end=' ')
#     for i in arr:
#         print(i, end=' ')
#     print()

# 해봤는데 안됨

from collections import deque
T = 10

for _ in range(T):
    tc = int(input())
    queue = deque(map(int, input().split()))
    i = 1
    while True:
        if i == 6:
            i = 1
        n = queue.popleft()
        n -= i
        if n <= 0:
            n = 0
            queue.append(n)
            break

        queue.append(n)
        i += 1

    print(f'#{tc}', end=' ')
    for i in queue:
        print(i, end=' ')
    print()