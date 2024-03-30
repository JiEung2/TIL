dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def to_bin(num):
    binary = ""
    for i in range(4):
        binary += str(num % 2)
        num //= 2

    return binary[::-1]

T = int(input())

for tc in range(T):
    n, number = input().split()
    result = ""
    for i in range(len(number)):
        if number[i].isdigit():
            result += to_bin(int(number[i]))
        else:
            result += to_bin(dic[number[i]])

    print(f'#{tc+1} {result}')
