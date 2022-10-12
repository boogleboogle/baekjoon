# 백준 1단계 입출력과 사칙연산
# 10430번 나머지

# 입력과 출력에 관한 문제

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

A, B, C = map(int, input().split())

# 이 문제에 어떤 의미가 있을까?
# https://st-lab.tistory.com/214 참고
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print( ((A%C) * (B%C))%C)

