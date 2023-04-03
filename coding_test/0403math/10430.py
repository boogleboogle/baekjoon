# 백준 코딩 테스트 준비 - 기초 - 수학
# 10430번 나머지

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
A, B, C = map(int, input().split())

# print(A, B, C)
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C)%C))
# N = int(input())
# list_N = list(map(int, input().split()))
# M = int(input())
# list_M = list(map(int, input().split()))

# list_N.sort()