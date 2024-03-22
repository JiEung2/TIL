dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
       'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def to_bin(n):
    binary = ''
    for _ in range(4):
        binary = str(n % 2) + binary
        n //= 2
    return binary

T = int(input())

for tc in range(T):
    n, arr = input().split()
    result = ""
    for i in range(len(arr)):
        result += to_bin(dic[arr[i]])
    print(f'#{tc+1} {result}')