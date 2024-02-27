# def run(level):
#     if level == 3:
#         return
#
#     for i in range(2):
#         run(level + 1)
#
# run(0)


# path = []
#
# def KFC(x):
#     if x == 2:
#         print(path)
#         return
#
#     for i in range(3):
#         path.append(i)
#         KFC(x + 1)
#         path.pop()
#
# KFC(0)


# path = []
#
# def recur(L):
#     if L == 3:
#         print(path)
#         return
#
#     for i in range(1, 7):
#         path.append(i)
#         recur(L + 1)
#         path.pop()
#
# recur(0)


path = []

def recur(L):
    if L == N:
        print(path)
        return

    for i in range(1, 7):
        if used[i]:
            continue
        used[i] = True
        path.append(i)
        recur(L + 1)
        path.pop()
        used[i] = False


used = [False for _ in range(7)]
N = input()
