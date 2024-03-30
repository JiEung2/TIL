def union(a, b):
    index1 = find(a)
    index2 = find(b)
    if index1 < index2:
        s[index2] = index1
    else:
        s[index1] = index2

def find(x):
    while x != s[x]:
        x = s[x]

    return x

T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]

    s = [i for i in range(n)]
    for i in range(m):
        union(arr[i][0]-1, arr[i][1]-1)

    result = set()
    for i in range(n):
        result.add(find(i))

    print(f'#{tc+1} {len(result)}')

