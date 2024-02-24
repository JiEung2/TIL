# def perm(k, sumV):
#     global min_V
#     if k == N:
#         if min_V > sumV:
#             min_V = sumV
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             perm(k+1, sumV + numbers[k][i])
#             visited[i] = False
#
# min_V = 100
# N = 3
# numbers = [[2, 1, 2], [5, 8, 5], [7, 2, 2]]
# visited = [False] * N
# perm(0, 0)
# print(min_V)

#
# T = int(input())
# for tc in range(1,T+1):
#     N, M = map(int, input().split())
#     pizzas = list(map(int, input().split()))
#     num_pizza = []
#     oven = []
#     for idx in range(M) :
#       num_pizza.append([idx+1, pizzas[idx]]) #피자번호, 피자 넣기
#
#     for put in range(N):
#         oven.append(num_pizza[put])
#
#     remain = num_pizza[N:]
#     # print(remain)
#     while len(oven) > 1 :
#         idx, cheese = oven.pop(0)
#         cheese //= 2
#         if cheese != 0 :
#             oven.append([idx, cheese])
#         else :
#             if remain:
#                 oven.append(remain.pop(0))
#     print(f'#{tc} {oven.pop()[0]}')


# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())  # N:보드 한 변의 길이, M:돌 놓는 횟수
#     board = [[0] * N for _ in range(N)]
#
#     # 보드의 정가운데에 흰,검/검,흰 놓기
#     board[N // 2 - 1][N // 2 - 1] = 2
#     board[N // 2 - 1][N // 2] = 1
#     board[N // 2][N // 2 - 1] = 1
#     board[N // 2][N // 2] = 2
#
#     for _ in range(M):
#         x, y, color = map(int, input().split())
#
#         board[x - 1][y - 1] = color
#         now_color = color
#         if now_color == 1:
#             reverse_color = 2
#         else:
#             reverse_color = 1
#
#         for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
#             nR = (x - 1) + dr
#             nC = (y - 1) + dc
#
#             while 0 <= nR < N and 0 <= nC < 0 and board[nR][nC] == reverse_color:
#                 nR += dr
#                 nC += dc
#
#             if 0 <= nR < N and 0 <= nC < 0 and board[nR][nC] == now_color:
#                 while nR != (x - 1) or nC != (y - 1):
#                     nR -= dr
#                     nC -= dc
#                     board[nR][nC] = now_color
#
#             # if 0 <= nR < N and 0 <= nC < N and board[nR][nC] != color and board[nR][nC] != 0 :
#             #     if 0 <= nR2 < N and 0 <= nC2 < N and board[nR2][nC2] == color:
#             #         board[nR][nC] = color
#             #         break
#     B = 0
#     W = 0
#     for row in range(N):
#         for col in range(N):
#             if board[row][col] == 1:
#                 B += 1
#             elif board[row][col] == 2:
#                 W += 1
#     print(f'#{tc} {B} {W}')





# def plus_flies(row, col):
#     dr = [-1 , 1, 0, 0]
#     dc = [0, 0, -1, 1]
#
#     arr_sum = 0
#     for jump in range(1, M+1):
#         for i in range(4):
#             new_row = row + dr[i] * jump
#             new_col = col + dc[i] * jump
#             if 0 <= new_row <= N-1 and 0 <= new_col <= N-1:
#                 arr_sum += arr[new_row][new_col]
#
#     return arr_sum
#
#
# def cross_flies(row, col):
#     dr = [-1, -1, 1, 1]
#     dc = [-1, 1, -1, 1]
#
#     arr_sum = 0
#     for jump in range(1, M + 1):
#         for i in range(4):
#             new_row = row + dr[i] * jump
#             new_col = col + dc[i] * jump
#             if 0 <= new_row <= N - 1 and 0 <= new_col <= N - 1:
#                 arr_sum += arr[new_row][new_col]
#
#     return arr_sum
#
#
# # 인풋
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split()) # N은 배열 크기, M은 파리 약의 세기
#     arr = [list(map(int, input().split())) for _ in range(N)] # 파리의 개수가 정해진 arr
#     # print(arr)
#     died_flies = [] # 잡을 수 있는 파리 갯수 저장
#
#
#     # 처음부터 쭉 돌면서 시작점 지정
#     for row in range(N):
#         for col in range(N):
#             # +형태로 잡을 수 있는 파리 개수 저장 변수에 시작점 넣고 시작
#             plus_sum = arr[row][col]
#             # +형태로 잡을 수 있는 파리의 위치에서 잡을 수 있는 값을 모두 더하여 리턴
#             plus_sum += plus_flies(row, col)
#             # 최대 비교를 위한 리스트에 추가
#             died_flies.append(plus_sum)
#
#             # X 형태로 잡을 수 있는 파리 개수 저장 변수에 시작점 넣고 시작
#             cross_sum = arr[row][col]
#             # X 형태로 잡을 수 있는 파리의 위치에서 잡을 수 있는 값을 모두 더하여 리턴
#             cross_sum += cross_flies(row, col)
#             # 최대 비교를 위한 리스트에 추가
#             died_flies.append(cross_sum)
#
#     print(f'#{tc} {max(died_flies)}')




# N = int(input())
# maxV = 0
# lst = [N]
# maxL = []
# # print(lst)
#
# for second_number in range(N//2, N+1):
#     lst.append(second_number)
#     index = 1
#     while lst[-1] >= 0:
#         lst.append(lst[index-1] - lst[index])
#         index += 1
#
#     lst.pop()
#     if maxV < len(lst):
#         maxV = len(lst)
#         maxL = lst
#     index = 1
#     lst = [N]
#
# print(maxV)
# for i in maxL:
#     print(i, end=" ")





# 색을 바꿀 좌표들의 리스트가 있음
# def change_color(will_change_list):
#     for row, col in will_change_list:
#         if arr[row][col] == 1:
#             arr[row][col] = 2
#         elif arr[row][col] == 2:
#             arr[row][col] = 1
#
# def check(row, col, color, dr, dc):
#     will_change_list = []
#     New_row = row + dr
#     New_col = col + dc
#     # 범위 안에 있고 현재 위치의 돌과 색이 다르고 빈칸이 아닌 동안 반복
#     while 0 <= New_row <= N-1 and 0 <= New_col <= N-1 and arr[New_row][New_col] != 0:
#         # 쭉 가다가 나랑 같은 색 돌을 만났다 -> 그 전까지 쌓인 흰색 돌의 좌표를 가져감
#         if arr[New_row][New_col] == color:
#             return will_change_list
#         # 다른 색깔 돌인 경우에는 좌표를 추가하고 다음 좌표 확인하러 감
#         else:
#             will_change_list.append((New_row, New_col))
#             New_row += dr
#             New_col += dc
#
#     # 범위 안에서 검은 돌인 걸 만나지 못한 경우 빈 리스트를 리턴
#     will_change_list = []
#     return will_change_list
#     # 어떻게 정상적으로 빠져나온 것과 아닌 것을 구분하지?
#
# T = int(input())
#
# for tc in range(1,T+1):
#     N, M = map(int, input().split()) # N = N*N, M = 돌 놓는 횟수
#     arr = [[0]*N for _ in range(N)]
#     # 정가운데 흑, 백돌 배치하기
#     start_row = N//2 - 1
#     start_col = N//2 - 1
#     for dr, dc in [(0, 0), (1, 1)]:
#         arr[start_row+dr][start_col+dc] = 1
#
#     for dr, dc in [(1, 0), (0, 1)]:
#         arr[start_row+dr][start_col+dc] = 2
#     # print(arr)
#
#     for i in range(M):
#         row, col, color = map(int, input().split())
#         row -= 1
#         col -= 1
#         arr[row][col] = color
#         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
#             # 색을 바꿀 좌표들의 리스트를 가져옴
#             change_color(check(row, col, color, dr, dc))
#
#     # 돌면서 각각 개수 확인해주기
#     cnt_B = 0
#     cnt_W = 0
#     for row in range(N):
#         for col in range(N):
#             if arr[row][col] == 1:
#                 cnt_B += 1
#             elif arr[row][col] == 2:
#                 cnt_W += 1
#
#     print(f'#{tc} {cnt_B} {cnt_W}')


