def bubble_sort(arr):
    for i in range(len(arr), 0, -1):
        for j in range(i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

T = int(input())

for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))

    new_numbers = bubble_sort(numbers)
    print(f'#{tc+1}', end=' ')
    for i in range(5):
        print(f'{new_numbers[len(new_numbers)-i-1]} {new_numbers[i]}', end=' ')
    print()
