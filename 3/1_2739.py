# 백준 3단계 반복문
# 2739번 구구단

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
N = int(input())

for i in range(1, 10):
    print(f"{N} * {i} = {N*i}")
