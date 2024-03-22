def binary_search(l, r, number, cnt):
    cnt += 1
    mid = int((l+r)/2)
    if mid == number:
        return cnt
    if mid > number:
        return binary_search(l, mid, number, cnt)
    else:
        return binary_search(mid, r, number, cnt)


T = int(input())
for tc in range(T):
    P, A, B = map(int, input().split())
    a = binary_search(1, P, A, 0)
    b = binary_search(1, P, B, 0)

    if a < b:
        result_cnt = 'A'
    elif a > b:
        result_cnt = 'B'
    else:
        result_cnt = 0

    print(f'#{tc+1} {result_cnt}')