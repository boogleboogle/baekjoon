# 백준 1단계 입출력과 사칙연산
# 10998번 A*B

# 입력과 출력에 관한 문제

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

A, B = map(int, input().split())

print(A*B)

