# 백준 4단계 1차원 배열
# 2562번 최댓값

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
import sys
list_input = []

for i in range(9):
    list_input.append(int(sys.stdin.readline()))

max_num = max(list_input)
print(max_num)
print(list_input.index(max_num)+1)
