# 백준 1단계 입출력과 사칙연산
# 2588번 곱셈

# 입력과 출력에 관한 문제

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# int, str로 받아서 활용한다.
A = int(input())
B = input()

print(A*int(B[2]))
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B))


