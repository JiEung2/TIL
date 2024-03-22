def combi(k, s):
    if k == K :
        print(result_cnt)
        sumV = 0
        for i in range(K):
            pos = result_cnt[i]
            sumV += numbers[pos]
        print(sumV)
        return

    for i in range(s, N-K+1+k):
        result_cnt[k] = i
        combi(k+1, i+1)

numbers = [8,1,9,7,2,5]
N = len(numbers)
K = 3
result_cnt = [-1] * K  #위치 인덱스
visited = [False]*N
combi(0, 0)