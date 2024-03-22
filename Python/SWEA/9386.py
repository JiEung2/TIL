# 연속한 1의 개수

'''
N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력하는 프로그램을 만드시오.
'''

T = int(input())

for tc in range(T):
    N = int(input())
    numbers = input()

    result_cnt = 0
    cnt = 0
    for i in range(N):
        if int(numbers[i]) == 1:
            cnt += 1
        if int(numbers[i]) == 0 or i == N-1:
            if result_cnt < cnt:
                result_cnt = cnt
            cnt = 0

    print(f'#{tc+1} {result_cnt}')