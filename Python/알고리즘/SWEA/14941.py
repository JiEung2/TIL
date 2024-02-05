T = int(input())

for tc in range(T):
    str1 = input()
    str2 = input()

    maxV = 0
    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt += 1

        if cnt > maxV:
            maxV = cnt
    print(f'#{tc+1} {maxV}')