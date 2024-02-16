# def bfs(x, y, Map):
#     q = []
#     q.append((x, y))
#     dx = [1, 0, -1, 0]
#     dy = [0, -1, 0, 1]
#
#     while q:
#         tx, ty = q.pop()
#         for d in range(4):
#             nx = tx + dx[d]
#             ny = ty + dy[d]
#
#             if 0 <= nx < 16 and 0 <= ny < 16 and Map[nx][ny] == 0:
#                 Map[nx][ny] = 1
#                 q.append((nx, ny))
#             elif 0 <= nx < 16 and 0 <= ny < 16 and Map[nx][ny] == 3:
#                 return 1
#
#     return 0
#
# T = 10
#
# for _ in range(T):
#     tc = int(input())
#     Map = [list(map(int, input())) for _ in range(16)]
#
#     result = 0
#     for i in range(16):
#         for j in range(16):
#             if Map[i][j] == 2:
#                 result = bfs(i, j, Map)
#
#     print(f'#{tc} {result}')


def bfs(r,c) :
    q = []
    visited = [[0]*16 for _ in range(16)]

    q.append((r,c))
    visited[r][c] = 1
    while q :
        vr, vc = q.pop(0)

        for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)] :
            newR = vr + dr
            newC = vc + dc
            if not visited[newR][newC] and 1<= newR <14 and 1<= newC < 14 and arr[newR][newC] != 1 :
                q.append((newR, newC))
                visited[newR][newC] = 1
                if arr[newR][newC] == 3 :
                    return 1
    return 0

T = int(input())
for tc in range(1,T+1) :
    arr = [list(map(int, input())) for _ in range(16)]

    for row in range(16):
        for col in range(16) :
            if arr[row][col] == 2 :
                R = row
                C = col
                break

    #for row in range(N) :
    #   if arr[row].count(2) :
    #       stc = arr[row].index(2)
    #       break
    print(f'#{tc} {bfs(R,C)}')