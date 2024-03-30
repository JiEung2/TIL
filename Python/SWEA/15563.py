def dfs(index, power, cnt):
    global result_cnt

    if cnt > result_cnt:
        return

    if index + power >= n:
        result_cnt = min(result_cnt, cnt)
        return

    for i in range(index + power, index, -1):
        if i >= n: continue
        dfs(i, arr[i], cnt + 1)

T = int(input())

for tc in range(T):
    result_cnt = float('inf')
    arr = list(map(int, input().split()))
    n = arr[0]

    dfs(1, arr[1], 0)
    print(f'#{tc+1} {result_cnt}')





# def subSet(k, battery, cnt):
#     global minV
#     if cnt >= minV:
#         return
#
#     if k == N:
#         if cnt < minV:
#             minV = cnt
#         return
#
#     if battery == 0:
#         return
#
#     subSet(k + 1, battery - 1, cnt)
#     subSet(k + 1, arr[k + 1], cnt + 1)
#
#
# T = int(input())
# for tc in range(T):
#     arr = list(map(int, input().split())) + [0]
#     N = arr[0]
#     minV = 100000
#     subSet(1, arr[1], 0)
#     print(f'#{tc + 1} {minV}')
