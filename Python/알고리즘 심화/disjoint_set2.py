def make_set(data):
    idx = datas.index(data)
    p[idx] = idx
    print(p)

# data가 포함된 셋의 대표의 index를 return
def find_set(data):
    idx = datas.index(data)
    while idx != p[idx]:
        idx = p[idx]
    return idx

def link(idx1, idx2):
    if rank[idx1] < rank[idx2]:
        p[idx1] = idx2
    else:
        p[idx2] = idx1
        if rank[idx1] == rank[idx2]:
            rank[idx1] += 1

def union(data1, data2):
    idx1 = find_set(data1)
    idx2 = find_set(data2)
    link(idx1, idx2)

def union_old(data1, data2):
    idx1 = find_set(data1)
    idx2 = find_set(data2)
    if idx1 < idx2:
        p[idx2] = idx1
    else:
        p[idx1] = idx1


datas = ['a', 'b', 'c', 'd', 'e', 'f']
p = [-1] * len(datas)
rank = [0] * len(datas)

for data in datas:
    make_set(data)

p[3] = 2
print(find_set('c'))
print(f'd의 대표는 {datas[find_set("d")]}')

union('c', 'd')
print(p)
union('e', 'f')
print(p)
union('d', 'f')
print(p)
print(find_set('d'))
print(find_set('e'))
print(find_set('f'))