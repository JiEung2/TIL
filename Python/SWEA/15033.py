def divide(i, j):
    if i == j:
        return i

    a = divide(i, (i+j)//2)
    b = divide((i+j)//2+1, j)

    return rockPaperScissors(a, b)

def rockPaperScissors(a, b):
    if arr[a] == arr[b]:
        return a
    elif arr[a] - arr[b] == 1 or arr[a] - arr[b] == -2:
        return a
    else:
        return b

T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    result = divide(0, N-1)
    print(f'#{tc+1} {result+1}')