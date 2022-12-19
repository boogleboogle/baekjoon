# K-Digital Training 코딩테스트 모의고사_2회차
# 2번 

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

# 구켓몬의 종류 n, 빵의 개수 m
n, m = map(int, sys.stdin.readline().split())

# print(n, m)

count = 0
sum_m = int(n*(n+1)/2)
# print(sum_m)

list_guketmon = [0 for i in range(n+1)]
# print(list_guketmon)

for i in range(m):
    bread_input = int(sys.stdin.readline())
    count += 1
    if list_guketmon[bread_input] == 0:
        list_guketmon[bread_input] = 1
        sum_m -= bread_input
    if sum_m == 0:
        break
if 0 in list_guketmon[1:]:
    count = -1
print(count)

