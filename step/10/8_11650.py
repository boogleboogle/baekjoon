# 백준 10단계 정렬
# 11650번 좌표 정렬하기

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
N = int(input())
list_input = []

for i in range(N):
    list_input.append(list(map(int, input().split())))

list_input_sorted = sorted(list_input)
# print(list_input_sorted)
for i in list_input_sorted:
    print(i[0], i[1])