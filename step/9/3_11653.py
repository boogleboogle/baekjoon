# 백준 9단계 기본 수학 2
# 11653번 소인수분해

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

N = int(input())



while True:
    if N == 1:
        break
    for i in range(2, N+1):
        if N%i == 0:
            print(i)
            N = int(N/i)
            break

