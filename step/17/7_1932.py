# 백준 17단계 동적 계획법 1
# 1912번 정수 삼각형

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

N = int(input())
list_input = []
for i in range(N):
    list_input.append(list(map(int, input().split())))
print(list_input)
dp = [[0, 0] for _ in range(N)]
dp[0][0] = list_input[0][0]
dp[0][1]= list_input[0][0]
print(dp)
