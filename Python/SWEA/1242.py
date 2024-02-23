def toBin(s):
    hex_mapping = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                   '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                   '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                   'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
                   }
    result = ''
    for c in s:
        result += hex_mapping[str(c)]

    return result

mapping = {'211': '0', '221': '1', '122': '2', '411': '3', '132': '4',
           '231': '5', '114': '6', '312': '7', '213': '8', '112': '9'}

# import sys
# sys.stdin = open("sample_input (3).txt", "r")
T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]
    result = 0
    real_code = []
    new_code = []

    for i in range(N):
        tmp = ''
        for j in range(M):
            tmp += toBin(code[i][j])
        new_code.append(tmp)

    for i in range(1, N):
        for j in range(len(new_code[i])-1, -1, -1):
            if new_code[i][j] == '1' and new_code[i-1][j] == '0':
                real_code.append(new_code[i][0:j+1])
                break

    print(real_code)
    for i in range(len(real_code)):
        bin_code = real_code[i][::-1]
        start = bin_code.find('1')
        now = 1
        cnt = [1] * 3
        tmp = []
        idx = 0
        for j in range(start+1, len(bin_code)):
            if str(now) == bin_code[j]:
                cnt[idx] += 1
            else:
                # tmp.append(str(cnt))
                now = abs(now - 1)
                if idx == 2:
                    min_v = min(cnt)
                    for c in cnt:
                        tmp += str(c // min_v)
                    idx = 0
                    cnt = [1] * 3
                else:
                    idx += 1

        # print(tmp)
        # tmp.append(str(cnt))
        tmp = tmp[::-1]
        print(tmp)

        code_list = []
        index = 0
        tmp_code = tmp[0:3]
        for j in range(3, len(tmp), 4):
            tmp_code = tmp[j: j+3]
            code_list.append(''.join(tmp_code))
            index += 1

        # result_bin = []
        # for z in range(len(code_list)):
            # min_value = float('inf')
            # for j in code_list[z]:
            #     if min_value > int(j):
            #         min_value = int(j)

            # if min_value > 1:
            #     for j in range(len(code_list[z])):
            #         code_list[z][j] = str(int(code_list[z][j]) // min_value)
            # result_bin.append(''.join(code_list[z]))
        print(code_list)
        result_int = ''
        for j in range(len(code_list)):
            result_int += mapping[code_list[j]]
        print(result_int)

        sum1 = 0
        sum2 = 0
        for j in range(0, 8, 2):
            sum1 += int(result_int[j])
            sum2 += int(result_int[j + 1])

        if (sum1 * 3 + sum2) % 10 == 0:
            result += sum1 + sum2

    print(f'#{tc + 1} {result}')