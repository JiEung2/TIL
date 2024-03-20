#이진탐색트리

#삽입
# def insert(value) :
#     pos = 1
#     while TREE[pos] != -1 :
#         if TREE[pos] > value :
#             pos *= 2
#         else :
#             pos = pos*2+1
#     TREE[pos] = value
#
# def inorder(rootP):
#     if TREE[rootP*2] != -1:
#         inorder(rootP*2)
#     print(TREE[rootP])
#     if TREE[rootP*+1] != -1 :
#         inorder(rootP*2+1)
#
#
# TREE = [-1]*100
# insert(9)
# insert(12)
# insert(15)
# insert(4)
# #print(TREE) #정렬된 순서로 나오려면 inorder
# inorder(1)

# #무조건 재귀 호출
# def insert(value):
#     pos = 1
#     while TREE[pos] != -1:
#         if TREE[pos] > value:
#             pos *= 2
#         else:
#             pos = pos * 2 + 1
#     TREE[pos] = value
#
# #key가 트리에 있으면 저장 idx가 없으면 -1 return
# def find(key) :
#     pos = 1
#     while TREE[pos] != -1:
#         if TREE[pos] == key :
#             return
#         if TREE[pos] < key :
#             pos = pos*2+1
#         else :
#             pos *= 2
#     return -1
#
# def inorder(rootP):
#     if TREE[rootP] != -1 :
#         inorder(rootP * 2)
#         print(TREE[rootP])
#         inorder(rootP * 2 + 1)
#
#
# TREE = [-1] * 100
# insert(9)
# insert(12)
# insert(15)
# insert(4)
# # print(TREE) #정렬된 순서로 나오려면 inorder
# inorder(1)


#힙
#완전이진트리여야 함!!

# 삽입
# def insert(value) :
#     global last
#
#     last += 1
#     TREE[last] = value
#
#     c = last
#     p = c//2
#     # while p >= 1 :
#     #     if TREE[p] < TREE[c]:
#     #         TREE[p], TREE[c] = TREE[c], TREE[p]
#     #         c = p
#     #         p = c//2
#     #     else :
#     #         break
#
#     while p >= 1 and TREE[p] < TREE[c]:
#         TREE[p], TREE[c] = TREE[c], TREE[p]
#         c = p
#         p = c//2
#     print(TREE)
#
#
# TREE = [0, 20,15,19,4,13,11] +[-1]*100
# # print(TREE)
# last = 6
# insert(17)
# insert(23)


def insert(value):
    global last

    last += 1
    TREE[last] = value

    c = last
    p = c // 2

    while p >= 1 and TREE[p] < TREE[c]:
        TREE[p], TREE[c] = TREE[c], TREE[p]
        c = p
        p = c // 2
    print(TREE)

def pop():
    global last
    t = TREE[1]
    TREE[1] = TREE[last]
    last -= 1

    p = 1
    c = p*2
    while c <= last :
        if c+1 <= last and TREE[c] < TREE[c+1] :
            c += 1
        if TREE[p] < TREE[c] :
            TREE[p], TREE[c] = TREE[c], TREE[p]
            p = c
            c = p*2
        else :
            break
    return t

TREE = [0, 20, 15, 19, 4, 13, 11] + [-1] * 100
# print(TREE)
last = 6
# insert(17)
# insert(23)
print(pop())
print(pop())