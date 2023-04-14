# 백준 10단계 정렬
# 2587번 대표값2

import sys
from tabnanny import check

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

list_input = []

for _ in range(5):
    list_input.append(int(input()))
# nlogn
for i in range(5):
    for j in range(5):
        if list_input[i] < list_input[j]:
            list_input[i], list_input[j] = list_input[j], list_input[i]


print(int(sum(list_input)/5))
print(list_input[2])