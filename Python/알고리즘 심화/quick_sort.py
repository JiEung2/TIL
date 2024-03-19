# s, e사이에서 s 위치의 값을 pivot으로
# 좌측에는 작은 값들이 우측에는 큰 값들을 모으고
# pivot의 위치를 return 한다

def partition_l(s, e):
    p = e
    i = s-1
    for j in range(s, e):
        if numbers[j] < numbers[p]:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[p] = numbers[p], numbers[i+1]
    return i+1

def partition_h(s, e):
    p = s
    i = s+1
    j = e
    # i의 위치 이동
    while i <= j:
        while i <= j and numbers[i] <= numbers[p]:
            i += 1
        # j의 위치 이동
        while i <= j and numbers[j] > numbers[p]:
            j -= 1

        if i < j:
            numbers[i], numbers[j] = numbers[j], numbers[i]

    numbers[p], numbers[j] = numbers[j], numbers[p]
    return j

def quick_sort(s, e):
    if s < e:
        m = partition_h(s, e)
        quick_sort(s, m-1)
        quick_sort(m+1, e)

numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
N = (len(numbers))
quick_sort(0, N-1)
print(numbers)