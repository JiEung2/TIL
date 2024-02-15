T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    index = M % N
    print(f'#{tc+1} {arr[index]}')