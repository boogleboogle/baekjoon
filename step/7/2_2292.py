# 백준 7단계 기본 수학 1
# 2292번 벌집

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

# 1부터 n까지의 거리는 육각형 중심에서부터의 거리를 나타낸 것이다.
# 동심원을 그린다는 생각으로 각 원의 둘레에서 가장 낮은 숫자의 규칙성을 찾아보자.
# 육각형의 각 변의 길이는 [1, 2, 3, 4, 5 ...]
# 육각형의 각 둘레의 길이는 [1, 6, 12, 18...]
# 물론 각 동심원에서 가장 낮은 숫자를 찾아 규칙을 찾을 수도 있지만, 다 그리기는 번거롭다.

# 시간초과로 다시 진행한다.
# 각 동심원에서 가장 낮은 숫자[1, 2, 8, 20, 38, 62]
# ==[1, 2] + [6*(index-1) + [index-1]]
# [:1] - 2 == [0, 6, 18, 36, 60...] == [6*0, 6*1, 6*3, 6*6, 6*10...]

# N(1 ≤ N ≤ 1,000,000,000)
N = int(input())

distance = 0

list_temp = [1]
temp = 0
for i in range(1, 20000):
    list_temp.append(6*temp + 2)
    temp += i
    if 6*temp > 1000000000:
        break

# print(list_temp[:10])

for i in list_temp:
    if i <= N:
        distance += 1

print(distance)








###################################################################
# # 시간초과
# N = int(input())

# distance = 1
# while True:
#     # print(distance)
#     # N이 1일 경우 더 이상 갈 곳이 없으니 break
#     if N == 1:
#         break
#     # N이 갈 거리가 남아있으면 진행한다.
#     elif N > 0:
#         # 갈 수 있으면
#         if N >=  distance * 6:
#             N -= distance * 6
#             distance += 1
#         # 갈수 없으면
#         else:
#             distance += 1
#             break


# print(distance)

