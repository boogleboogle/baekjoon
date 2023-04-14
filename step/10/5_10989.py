# 백준 10단계 정렬
# 10989번 수 정렬하기 3

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
# N = int(input())
# list_input = []

# for _ in range(N):
#     list_input.append(int(input()))
# # list_temp = sorted(list_input)
# list_input.sort()

# for i in list_input:
#     print(i)
# 메모리 초과

import sys
n = int(sys.stdin.readline())
b = [0] * 10001
for i in range(n):
    b[int(sys.stdin.readline())] += 1
for i in range(10001):
    if b[i] != 0:
        for j in range(b[i]):
            print(i)