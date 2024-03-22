def dfs(cnt, sum_height):
    global ans
    # 기저조건


    # 2. 키의 합이 B 이상이면 종료
    # -> 현재까지 쌓은 탑의 높이
    if sum_height >= B:
        # 제일 높이가 낮은 탑이 정답
        # - 최소 탑의 높이는 재귀호출 함수들이 "동시에" 사용함 -> 전역변수로 사용
        ans = min(ans, sum_height)
        return

    # 1. 모든 점원이 탑을 쌓는데 고려가 되었다면
    #   -> 현재까지 쌓은 점원의 수
    if cnt == N:
        return
    # 재귀호출파트
    # 쌓는다 안쌓는다
    dfs(cnt + 1, sum_height + arr[cnt])
    dfs(cnt + 1, sum_height)

T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = int(1e9)
    dfs(0, 0)
    print(abs(ans - B))