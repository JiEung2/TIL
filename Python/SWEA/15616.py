def find_set(person):
    idx = people.index(person)
    while idx != p[idx]:
        idx = p[idx]
    return idx


def union(data1, data2):
    idx1 = find_set(data1)
    idx2 = find_set(data2)

    if idx1 < idx2:
        p[idx2] = idx1
    else:
        p[idx1] = idx2

T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    people = [i for i in range(n)]
    p = [i for i in range(n)]

    result_cnt = set()
    for i in range(0, len(lst), 2):
        union(lst[i]-1, lst[i+1]-1)

    for i in range(n):
        result_cnt.add(find_set(i))

    print(f'#{tc+1} {len(result_cnt)}')