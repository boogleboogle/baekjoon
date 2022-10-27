# 백준 10단계 정렬
# 2751번 수 정렬하기 2

import sys
from tabnanny import check

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
N = int(input())
list_input = []

for _ in range(N):
    list_input.append(int(input()))
list_temp = sorted(list_input)

for i in list_temp:
    print(i)