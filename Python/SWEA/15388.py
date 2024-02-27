def check(card):
    for i in range(len(card)):
        if card[i] >= 3:
            return True

    cnt = 0
    for i in range(len(card)):
        if card[i] >= 1:
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            return True
    return False

T = int(input())

for tc in range(T):
    lst = list(map(int, input().split()))
    card1 = [0] * 10
    card2 = [0] * 10
    result = 0

    for i in range(0, len(lst), 2):
        card1[lst[i]] += 1
        if check(card1):
            result = 1
            break
        card2[lst[i+1]] += 1
        if check(card2):
            result = 2
            break

    print(f'#{tc+1} {result}')