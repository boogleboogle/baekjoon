# 백준 6단계 문자열
# 2675번 문자열 반복

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

test_case = int(input())

# print(test_case)
for t in range(test_case):
    R_S = input()

    R = int(R_S[0])

    S = R_S[2:]

    result = ""

    for i in S:
        result = result + i*R
    
    print(result)
        
