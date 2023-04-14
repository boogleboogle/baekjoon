# 백준 17단계 동적 계획법 1
# 1912번 연속합

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

N = int(input())
list_input = list(map(int, input().split()))

list_p = [0 for _ in range(N)]

list_p[0] = list_input[0]

for i in range(1, N):
    if list_input[i] + list_p[i-1] > 0:
        list_p[i] = list_input[i] + list_p[i-1]
    else:
        list_p[i] = list_input[i]

# print(list_input)
# print(list_p)
print(max(list_p))
# 틀렸습니다