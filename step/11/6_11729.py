# 백준 11단계 재귀
# 11729번 하노이 탑 이동 순서

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# # 여기부터 제출해야 한다.
def hanoi(n, start, end):
    # A 파트
    if n > 1:
        print("A")
        hanoi(n-1, start, 6-start-end)            
                         
    print(start, end)

    # B 파트
    if n > 1:
        print("B")
        hanoi(n-1, 6-start-end, end)

n = int(input())

print(2**n -1)                               
hanoi(2, 1, 3) 

# 13
# 12
# 32
# 13
# 21
# 23
# 13