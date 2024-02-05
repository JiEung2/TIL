T = int(input())

for tc in range(T):
    str1 = input()
    str2 = input()

    i = 0
    result = 0
    if str1 in str2:
        result = 1

    print(f'#{tc+1} {result}')