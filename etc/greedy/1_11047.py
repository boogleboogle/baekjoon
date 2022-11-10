# 백준 강의 알고리즘 중급1/3 710-그리디 알고리즘
# 11047번 동전 0

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

N, K = map(int, input().split())

list_coin = [int(input().rstrip()) for _ in range(N)][::-1]

# count = 0
# while K != 0:
#     # for coin in list_coin:
#     #     if K >= coin:
#     #         K -= coin
#     #         count += 1
#     #         break
#     coin = list_coin[0]
#     if K >= coin:
#         K -= coin
#         count += 1
#     else:
#         list_coin.pop(0)

# print(count)
# 시간초과

count = 0
for i in range(N):
    count += K//list_coin[i] 
    K = K%list_coin[i] 

print(count)