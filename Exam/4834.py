T = int(input())

for tc in range(T):
    n = int(input())
    numbers = list(map(int, input()))

    count = [0] * 10
    for number in numbers:
        count[number] += 1

    maxV = 0
    maxI = 0
    for i in range(9, 0, -1):
        if count[i] > maxV:
            maxV = count[i]
            maxI = i

    print(f'#{tc+1} {maxI} {maxV}')