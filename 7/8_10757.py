# 백준 7단계 기본 수학 1
# 10757번 큰 수 A+B

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

# 무슨 의도였을까?
A, B = map(int, input().split())

print(sum([A, B]))
