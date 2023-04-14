# 백준 3단계 반복문
# 10950번 A+B - 3

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

N = int(input())

list_input = []

for i in range(0, N):
    list_input.append(list(map(int, input().split())))


for i in list_input:
    print(sum(i))