# 백준 2단계 조건문
# 14681번 사분면 고르기

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
# 조건문에 and 와 or을 활용할 수 있는지 물어보는 문제였다.
input_x = int(input())
input_y = int(input())

if input_x > 0 and input_y > 0:
    print(1)
elif input_x < 0 and input_y > 0:
    print(2)
elif input_x < 0 and input_y < 0:
    print(3)
else:
    print(4)
