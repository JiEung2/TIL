mapping = {'0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4',
           '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'}
T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]
    s = ''
    flag = False
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if code[i][j] == '1':
                s = code[i][j-56+1: j+1]
                flag = True
                break
        if flag:
            break

    i_code = ''
    for i in range(0, 56, 7):
        tmp = s[i:i+7]
        i_code += mapping[tmp]

    sum1 = 0
    sum2 = 0
    for i in range(0, 8, 2):
        sum1 += int(i_code[i])
        sum2 += int(i_code[i+1])
    result = 0
    if (sum1*3 + sum2) % 10 == 0:
        result = sum1 + sum2

    print(f'#{tc+1} {result}')