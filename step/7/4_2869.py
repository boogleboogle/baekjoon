# 백준 7단계 기본 수학 1
# 2869번 달팽이는 올라가고 싶다

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

# A만큼 올라간다.
# B만큼 내려간다.
# V만큼 올라가야 한다.

import math
A, B, V = map(int, input().split())


day = (V-B) / (A-B)
# 오름
print(math.ceil(day))










# # 올라가면 떨어지지 않는다.
# V -= A
# day = 1

# # 남은 날에 올라간다.
# C = A - B

# # print(V/C)
# if int(V/C) < 1:
#     day += 1
# elif int(V/C) == V/C:
#     day += int(V/C) + 1
# else:
#     day += int(V/C)

# # print(C)
# print(day)
# # 14% 틀렸습니다.












