# 백준 4단계 1차원 배열
# 3052번 나머지

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
import sys
list_input = []

for i in range(10):
    list_input.append(int(sys.stdin.readline()))

s_input = set()
for i in list_input:
    s_input.add(i%42)

print(len(s_input))
