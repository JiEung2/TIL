#트리
# def preorder(root) :
#     print(root)
#     if len(TREE[root]) :
#         preorder(TREE[root][0])
#     if len(TREE[root]) >1:
#         preorder(TREE[root][1])

# def postorder(root) :
#     if len(TREE[root]) :
#         postorder(TREE[root][0])
#     if len(TREE[root]) >1:
#         postorder(TREE[root][1])
#     print(root)

def inorder(root) :
    if len(TREE[root]) :
        inorder(TREE[root][0])
    print(root)
    if len(TREE[root]) >1:
        inorder(TREE[root][1])



s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int, s.split()))
N = 13
TREE = [[] for _ in range(N+1)]
for i in range(0, len(lst), 2) :
    p = lst[i]
    c = lst[i+1]
    TREE[p].append(c)
# print(TREE)
# preorder(1)
# postorder(1)
inorder(1)