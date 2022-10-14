# 백준 3단계 반복문
# 8393번 합

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

N = int(input())

list_input = list(range(N+1))

print(sum(list_input))
