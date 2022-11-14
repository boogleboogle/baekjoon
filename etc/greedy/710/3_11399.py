# 백준 강의 알고리즘 중급1/3 710-그리디 알고리즘
# 11399번 ATM

from ctypes.wintypes import PINT
import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

N = int(input())

list_wating = list(map(int, input().split()))
list_wating.sort()
time = 0
for i in range(N):
    time += list_wating[i] * (N-i)
    # print(time)


# print(list_wating)
print(time)