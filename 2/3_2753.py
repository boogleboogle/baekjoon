# 백준 2단계 조건문
# 2753번 윤년

# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
# 조건문에 and 와 or을 활용할 수 있는지 물어보는 문제였다.
input_year = int(input())

if input_year%4 == 0 and input_year%100 != 0 or input_year%400 == 0:
    print(1)
else:
    print(0)