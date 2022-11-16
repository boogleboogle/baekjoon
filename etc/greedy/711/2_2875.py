# 백준 강의 알고리즘 중급1/3 711-그리디 알고리즘
# 2875번 대회 or 인턴

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

# 여학생, 남학생, 인턴쉽 인원
N, M, K = map(int, input().split())

team = 0

while True:
    people = N + M
    
    # 팀을 짤 사람이 부족하면 break한다.
    if people < 3 + K:
        break


    if N < 2:
        break
    else:
        N -= 2
    
    if M < 1:
        break
    else:
        M -= 1
    

    team += 1


print(team)
    





