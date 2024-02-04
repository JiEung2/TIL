T = int(input())

for tc in range(T):
    D, A, B, F = map(int, input().split())

    print(f'#{tc+1} {D / (A+B) * F}')
