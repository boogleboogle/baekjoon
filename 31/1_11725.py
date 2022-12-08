# 백준 17단계 동적 계획법 1
# 24416번 알고리즘 수업 - 피보나치 수 1

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))

cnt = {}

for i in a:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in b:
    if i in cnt:
        print(cnt[i], end=" ")
    else:
        print(0, end=" ")