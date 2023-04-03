# 백준 코딩 테스트 준비 - 기초 - 수학
# 4375번 1

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
# 2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때,
#  1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.

# 1로만 이루어진 n의 배수가 무슨 말일까?
# 알 수가 없다.

input_list = []
for i in range(3):
    n = int(input().strip())
    input_list.append(n)

print(input_list)

