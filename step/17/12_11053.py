# 백준 17단계 동적 계획법 1
# 24416번 알고리즘 수업 - 피보나치 수 1

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

n = int(input())
a = list(map(int, input().split()))
print(a)
dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))