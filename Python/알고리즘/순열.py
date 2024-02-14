def subSet(k, midS):
    if k == N:
        print(check)
        print(midS)
        return

    for i in [0, 1]:
        check[k] = i
        if i == 0:
            subSet(k + 1, midS)
        else:
            subSet(k + 1, midS+numbers[k])


N = 3
numbers = [10, 30, 20]
check = [-1] * N
subSet(0)
