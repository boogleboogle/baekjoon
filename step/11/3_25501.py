# 백준 11단계 재귀
# 11729번 하노이 탑 이동 순서

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# # 여기부터 제출해야 한다.
def hanoi(n, start, end):
    # 1. n번 째 블록을 end에 가져다 놓는 것과
    # 2. n-1번 째 블록을 나머지(6-start-end)에 가져다 놓는 것의 반복이다.

    # A 파트
    if n > 1:
        # print("A")
        hanoi(n-1, start, 6-start-end)            

    # 가장 위의 블록을 end로 옮긴다. 
    print(n, start, end)

    # B 파트
    # end를 비운다.
    if n > 1:
        # print("B")
        hanoi(n-1, 6-start-end, end)

n = int(input())

print(2**n -1)         
# 목표는 n개의 탑을 1에서 3으로 가져다 놓는 것이다.
hanoi(n, 1, 3) 

# 13
# 12
# 32
# 13
# 21
# 23
# 13