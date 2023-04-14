# 백준 2단계 조건문
# 2480번 주사위 세개

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
A, B, C = map(int, input().split())

if A == B == C:
    result = 10000 + A*1000
elif A == B or C== A:
    result = 1000 + A * 100
elif B == C:
    result = 1000 + B * 100
else:
    result = max(A, B, C)*100

print(result)
