# 백준 6단계 문자열
# 2908번 상수

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
A, B = input().split()

A = int(A[::-1])
B = int(B[::-1])

print(max(A,B))

