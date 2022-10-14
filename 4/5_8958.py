# 백준 4단계 1차원 배열
# 18958번 OX퀴즈

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
import sys
N = int(sys.stdin.readline())

def get_total_score():

    OX_input = input()
    score = 0
    total_score = 0
    for i in range(len(OX_input)):
        if OX_input[i] == "O":
            score += 1
            total_score += score
        else:
            score = 0
    print(total_score)

for i in range(N):
    get_total_score()