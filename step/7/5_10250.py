# 백준 7단계 기본 수학 1
# 10250번 ACM 호텔

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

T = int(input())

for i in range(T):

    # 층수, 방수, 몇 번째 손님
    H, W, N = map(int, input().split())

    # 몫, 나머지
    X, Y = divmod(N, H)
    X += 1

    # 손님이 층으로 나누어 떨어질 때.
    if Y == 0:
        Y = H
        X = X -1

    # 자리수 정리
    if len(str(X)) == 1:
        X = "0"+str(X)

    print(f"{Y}{X}")

# 문제 잘못읽음
##########################################
# # 호텔의 모양을 가로로 긴 형태로 만든다.
# check_change = 0
# if H > W:
#     H, W = W, H
#     check_change = 1

# Sum_HW = H + W

# # 호텔 모양의 2차원 리스트를 만든다.
# list_hotel = []
# for i in range(0, 2 + H):
#     list_temp = []
#     for j in range(0, 2 + W):
#         list_temp.append(-2)

#     list_hotel.append(list_temp)

# # test = 1
# for i in range(1, 1 + H):
#     for j in range(1, 1 + W):
#         list_hotel[i][j] = -1
#         # list_hotel[i][j] = test
#         # test += 1


# pprint.pprint(list_hotel)

# # 호텔에 손님을 배치한다.
# # 현재위치 X, Y
# X, Y = 1, 1
# num_guest = 1
# list_hotel[Y][X] = 1

# break_point = 0
# while True:
#     # 좌하단으로 움직일 수 있으면 이동한다.
#     if list_hotel[Y+1][X-1] == -1:
#         Y += 1
#         X -= 1
#         num_guest += 1
#         list_hotel[Y][X] = num_guest
#     # 좌상단에 자리가 없으면 낮은 층으로 이동한다.
#     else:
#         for i in range(1, 1 + H):
#             for j in range(1, 1 + W):
#                 if list_hotel[i][j] == -1:
#                     Y = i
#                     X = j
#                     break_point = 1
#                     num_guest += 1
#                     list_hotel[Y][X] = num_guest
#                     break
#             if break_point == 1:
#                 break
#     if num_guest == N:
#         break
#     print(num_guest)

# pprint.pprint(list_hotel)    
# print(Y, X)












