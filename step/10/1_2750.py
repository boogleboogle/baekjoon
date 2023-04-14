# 백준 10단계 정렬
# 2750번 수 정렬하기

import sys
from tabnanny import check

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

N = int(input())
list_input = []

for _ in range(N):
    list_input.append(int(input()))
# n^2
for i in range(N):
    for j in range(N):
        if list_input[i] < list_input[j]:
            list_input[i], list_input[j] = list_input[j], list_input[i]


for i in list_input:
    print(i)