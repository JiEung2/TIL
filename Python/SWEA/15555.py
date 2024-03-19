def merge(left, right):
    new_lst = []
    lp = 0
    rp = 0
    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            new_lst.append(left[lp])
            lp += 1
        else:
            new_lst.append(right[rp])
            rp += 1

    new_lst.extend(left[lp:])
    new_lst.extend(right[rp:])

    return new_lst

def merge_sort(arr):
    global cnt
    if len(arr) <= 1:
        return arr

    m = len(arr) // 2
    left = merge_sort(arr[:m])
    right = merge_sort(arr[m:])

    if left[-1] > right[-1]: cnt += 1
    new_lst = merge(left, right)
    return new_lst

T = int(input())

for tc in range(T):
    cnt = 0
    n = int(input())
    lst = list(map(int, input().split()))

    result = merge_sort(lst)
    print(f'#{tc+1} {result[n//2]} {cnt}')
