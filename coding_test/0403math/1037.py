# 백준 코딩 테스트 준비 - 기초 - 수학
# 1037번 약수

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
# N의 진짜 약수가 모두 주어질 때, N을 구하여라.

# N은 진짜 약수의 개수
N = int(input())
input_list = list(map(int, input().split()))

print(N, input_list)
# 인수분해 코드 찾기