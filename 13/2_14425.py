# 백준 13단계 집합과 맵
# 14425번 문자열 집합

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
# N, M = map(int, input().split())
# set_N = []
# for i in range(N):
#     set_N.append(input().rstrip())
# set_N = set(set_N)

# set_M = []
# for i in range(M):
#     set_M.append(input().rstrip())
# set_M = set(set_M)

# list_L = list(set_N & set_M)

# print(len(list_L))
# # 왜 틀림?

N, M = map(int, input().split())
s = set([input() for _ in range(N)])
cnt = 0
for _ in range(M):
    t = input()
    if t in s:
        cnt += 1
print(cnt)