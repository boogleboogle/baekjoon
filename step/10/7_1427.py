# 백준 10단계 정렬
# 1427번 소트인사이드

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
input_list = list(input())
input_list = list(int(i) for i in input_list)
input_list_sorted = sorted(input_list, reverse=True)

for i in input_list_sorted:
    print(i, end="")