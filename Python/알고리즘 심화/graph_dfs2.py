# 인접 리스트 DFS
graph = [
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3],
]

visited = [0] * 5
path = []

def dfs(now):
    # 기저 조건
    # 지금 문제에선 없다!

    # 다음 재귀 호출 전
    # visited[now] = 1
    # path.append(now)

    # 다음 재귀 호출
    # 인접 리스트
    # 차이점1. 갈 수 없는 곳 조건 필요없음
    # 차이점2. for문 작성 시 인덱스 사용 필요 없다.
    for to in graph[now]:
        # 이미 방문했다면 pass
        if visited[to]:
            continue

        visited[to] = 1
        path.append(to)
        dfs(to)

    # 돌아왔을 때 작업

# 출발점초기화
visited[0] = 1
path.append(0)
dfs(0)
print(path)