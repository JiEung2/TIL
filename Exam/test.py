# for tc in range(1, 11) :
#     input()
#     arr = [list(map(int, input().split())) for _ in range(100)]
#
#     #각 행의 합을 구한다
#     maxV = 0
#     for row in range(100) :
#         sumR = 0
#         for col in range(100) :
#             sumR += arr[row][col]
#         if maxV <= sumR :
#             maxV = sumR
#
#     #각 열의 합을 구한다
#     for col in range(100) :
#         sumC = 0
#         for row in range(100) :
#             sumC += arr[row][col]
#         if maxV <= sumC :
#             maxV = sumC
#
#     #우하향 대각선의 합을 구한다
#     # 좌하향 대각선의 합을 구한다
#     sumRCROSS = 0
#     sumLCROSS = 0
#     for row in range(100) :
#         sumRCROSS += arr[row][row]
#         sumLCROSS += arr[row][99-row]
#     if maxV <= sumRCROSS :
#         maxV = sumRCROSS
#     if maxV <= sumLCROSS :
#         maxV = sumLCROSS
#
#     print(f'#{tc} {maxV}')



# def censorship(key, value):
#     if key in black_list:
#         print(f'{key} 소속의 {value} 은/는 등록할 수 없습니다.')
#         return False
#     else:
#         print(f'이상 없습니다.')
#         return True
#
# def create_user(userlst):
#     censored_user_list = {}
#     for idx in range(len(userlst)):
#         newdic_key = userlst[idx]['company_name']
#         newdic_value = [userlst[idx]['name']]
#         if censorship(newdic_key, newdic_value):
#             censored_user_list[newdic_key] = newdic_value


# import sys
# sys.stdin = open("1216_input.txt","r")
#
#
# def check(arr, N, M):
#     for row in range(N):
#         for start in range(N - M + 1):
#             if arr[row][start:start + M] == arr[row][start:start + M][::-1]:
#                 return M
#
#     for col in range(N):
#         col_list = []
#         for row in range(N):
#             col_list.append(arr[row][col])
#         for start in range(N - M + 1):
#             if col_list[start:start + M] == col_list[start:start + M][::-1]:
#                 return M
#     return -1
#
#
# T = 10
# for _ in range(1, T+1):
#     tc = int(input())
#     N = 100
#     arr = [list(map(str, input())) for _ in range(N)]
#
#     for M in range(99,0,-1):
#         if check(arr,N,M) > 0:
#             print(check(arr, N, M))
#             break





# T =10
# for _ in range(1,T+1):
#     tc = int(input())
#     N = 100
#     arr = [input() for _ in range(N)]
#
#     ans = -1
#     for m in range(99, 0, -1) :
#
#         for row in range(N) :
#             for s in range(N-m+1):
#                 if arr[row][s:s+m] == arr[row][s:s+m][::-1]:
#                     ans = m
#                     break
#             if ans != -1 :
#                 break
#         if ans != -1:
#             break
#
#         for col in range(N):
#             newlst = []
#             for row in range(N):
#                 newlst.append(arr[row][col])
#             for s in range(N-m+1):
#                 if newlst[s:s+m] == newlst[s:s+m][::-1] :
#                     ans = m
#                     break
#             if ans != -1:
#                 break
#         if ans != -1:
#             break
#
#     print(f'#{tc}', ans)