def binary_search(s, e, number, sum, flag):
    if s > e:
        return -1
    m = (s + e) // 2
    if A[m] == number:
        return sum
    while s <= e:
        if A[m] < number:
            if flag == 1: return -1
            return binary_search(m + 1, e, number, sum + 1, 1)
        else:
            if flag == 2: return -1
            return binary_search(s, m - 1, number, sum + 1, 2)

T = int(input())

for tc in range(T):
    cnt = 0
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))

    for i in range(m):
        tmp = binary_search(0, n-1, B[i], 0, 0)
        if tmp >= 0:
            cnt += 1

    print(f'#{tc+1} {cnt}')

