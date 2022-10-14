# 백준 3단계 반복문
# 25304번 영수증

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

# 영수증에 적힌 금액 X
X = int(input())
# 구매한 물건의 종류의 수 N
N = int(input())

list_input = []

for i in range(0, N):
    list_input.append(list(map(int, input().split())))

prices = 0
for i in list_input:
    prices += i[0] * i[1]

if prices == X:
    print("Yes")
else:
    print("No")