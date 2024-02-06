T = int(input())

for tc in range(T):
    s = input()
    result = 0

    if s == s[::-1]:
        result = 1

    print(f'#{tc+1} {result}')