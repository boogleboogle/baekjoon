# 백준 10단계 정렬
# 11651번 좌표 정렬하기 2

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
N = int(input())
list_input = []

for i in range(N):
    list_input.append(list(map(int, input().split())))

for i in list_input:
    i[0], i[1] = i[1], i[0]

list_input_sorted = sorted(list_input)
# print(list_input_sorted)
for i in list_input_sorted:
    print(i[1], i[0])