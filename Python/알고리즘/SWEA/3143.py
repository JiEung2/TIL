T = int(input())

for tc in range(T):
    A, B = input().split()

    cnt = 0
    i = 0
    while i < len(A):
        if A[i:i+len(B)] == B:
            cnt += 1
            i += len(B)
        else:
            i += 1

    result = len(A) - (len(B) * cnt) + cnt
    print(f'#{tc+1} {result}')