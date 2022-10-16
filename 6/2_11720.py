# 백준 6단계 문자열
# 11720번 숫자의 합

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

N = int(input())

number_input_str = input()

result = 0
for i in number_input_str:
    result += int(i)

print(result)