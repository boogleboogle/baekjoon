# 백준 10단계 정렬
# 10814번 나이순 정렬

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
N = int(input())
list_input = []

for i in range(N):
    input_temp = input().split()
    list_input.append([int(input_temp[0]), input_temp[1]])

list_input_sorted = sorted(list_input, key=lambda x : (x[0]))
# print(list_input_sorted)

for i in list_input_sorted:
    print(*i)