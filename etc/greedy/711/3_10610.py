# 백준 강의 알고리즘 중급1/3 711-그리디 알고리즘
# 10610번 30

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

N = input()

# 30의 배수는 10의 배수이면서 3의 배수
# 1. 0이 포함되어야 한다.
# 2. 각 자리수의 합이 3의 배수여야 한다.

list_N = []
for i in N:
    list_N.append(int(i))

if 0 in list_N and sum(list_N)%3 == 0:
    list_N.sort(reverse=True)
    for i in list_N:
        print(i, end="")
else:
    print(-1)
# print(list_N)