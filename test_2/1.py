# K-Digital Training 코딩테스트 모의고사_2회차
# 1번 

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

n = int(input())
# n = 9
list_n = []
list_n_2 = []
for i in range(1, int(n/2)+1):
    list_n.append(i)
    list_n_2.append(n-i)
# print(list_n)
# print(list_n_2)

# 1일 경우를 무조건 포함한다.
count = 1
for i in range(1, len(list_n)):
    if list_n_2[i] % list_n[i] == 0:
        pass
    else:
        count += 1

print(count)

# 점수 안나옴

# 3
# 12

# 5
# 14
# 23

