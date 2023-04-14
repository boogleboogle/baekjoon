# 백준 5단계 함수
# 15596번 정수 N개의 합

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

def solve(a):
    ans = sum(a)
    return ans