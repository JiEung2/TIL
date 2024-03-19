def partition(s, e):
    p = s
    i = s + 1
    j = e
    while i <= j:
        while i <= j and lst[i] <= lst[p]:
            i += 1
        while i <= j and lst[j] > lst[p]:
            j -= 1

        if i < j:
            lst[i], lst[j] = lst[j], lst[i]

    lst[j], lst[p] = lst[p], lst[j]
    return j

def quick_sort(s, e):
    if s < e:
        m = partition(s, e)
        quick_sort(s, m-1)
        quick_sort(m+1, e)
T = int(input())

for tc in range(T):
    n = int(input())
    lst = list(map(int, input().split()))
    quick_sort(0, n-1)

    print(f'#{tc+1} {lst[n//2]}')
