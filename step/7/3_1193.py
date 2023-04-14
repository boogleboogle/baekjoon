# 백준 7단계 기본 수학 1
# 2292번 분수찾기

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

N = int(input())

# A/B 형태의 분수라고 한다.
# list_temp는 1/n 형태의 숫자들이 가지는 n 번째 수
list_temp = []
temp = 1
for i in range(1, 5000):
    list_temp.append(temp)
    temp += i
    if temp > 10000000:
        break

# print(list_temp[:10])


# C = A + B
C = 0
for i in list_temp:
    if i > N:
        break
    else:
        C = list_temp.index(i) + 2
        C_distance = N - i + 1

        # print(C)
        # 지그재그로 순서를 매긴다
        if C%2 == 0:
            B = C_distance
            A = C - C_distance
        else:
            A = C_distance
            B = C - C_distance
            
print(f"{A}/{B}")







