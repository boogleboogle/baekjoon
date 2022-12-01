# 백준 17단계 동적 계획법 1
# 11053번 가장 긴 증가하는 부분 수열

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

N = int(input())
for i in range(N):
    n = int(input())
    dp = [0] * 1000001
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2

    for k in range(6,n+1):
        dp[k] = (dp[k-1]+ dp[k-5])
    print(dp[n])