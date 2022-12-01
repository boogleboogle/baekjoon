# 백준 17단계 동적 계획법 1
# 1149번 RGB거리

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

# N = int(input())
# dp = []
# dp_2 = [[0, 0, 0] for _ in range(N)]
# # print(dp_2)
# for i in range(N):
#     dp.append(list(map(int, input().split())))

# print(dp)

# dp_2[0][0] = dp[0][0]
# dp_2[0][1] = dp[0][1]
# dp_2[0][2] = dp[0][2]

# for i in range(1, N):
#     dp_2[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
#     dp_2[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
#     dp_2[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]

# print(dp_2)
# print(min(dp_2[N-1]))

n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]
print(dp)
print(min(dp[n-1]))