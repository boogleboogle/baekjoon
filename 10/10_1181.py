# 백준 10단계 정렬
# 11651번 좌표 정렬하기 2

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
N = int(input())
list_input = []

for i in range(N):
    list_input.append(input().rsplit()[0])

# 중복제거
set_input = set(list_input)
list_input = list(set_input)

# 사전순 정렬
list_input_sorted = sorted(list_input)

# 길이순 정렬
list_input_sorted.sort(key=len)

# print(list_input_sorted)
for i in list_input_sorted:
    print(i)