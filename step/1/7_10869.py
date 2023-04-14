# 백준 1단계 입출력과 사칙연산
# 10869번 사칙연산

# 입력과 출력에 관한 문제

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

A, B = map(int, input().split())
a, b = divmod(A, B)

print(A+B)
print(A-B)
print(A*B)
print(a)
print(b)

