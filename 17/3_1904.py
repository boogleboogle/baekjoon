# 백준 17단계 동적 계획법 1
# 24416번 알고리즘 수업 - 피보나치 수 1

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

# 9184 1 00, 11 001, 100, 111 0011, 0000, 1001, 1100, 1111 만약 0과 1이라면
# 2^(n)
# 00이 하나 포함될 때마다 길이가 하나씩 줄어든다. 예를들어서
# n=1이라면 2여야 하지만 n=1일때 1, n=0일때 0 이므로 1 하나밖에 없다. 1
# n=2라면 11 0
# n=3이라면 111 10 01
# n=4라면 1111 110 101 011 00
# n=5라면 11111 1110 1101 1011 0111 100 010 001 
# 0이 2개 들어가는 2자리 숫자의 경우의 수 0이 1개 들어가는 3자리 숫자의 경우의 수 0이 0개 들어가는 4자리 숫자의 경우의 수
# n=n이라면
# 0이 int(n/2)개 들어가는 int(n/2+1)자리 숫자의 경우의 수 ~~ 0이 0개 들어가는 n자리 숫자의 경우의 수

# 그럼 부분을 이용하여 전체를 만들 수 있는지 생각 해 보자.
# ..1 2 3 5 8 피보나치 수열

n = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for k in range(3,n+1):
    dp[k] = (dp[k-1]+ dp[k-2])%15746
print(dp[n])