# 백준 7단계 기본 수학 1
# 1712번 손익분기점

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
# A는 고정비용
# B는 가변비용
# C는 판매가격

A, B, C = map(int, input().split())

profit = 0
count = 0

# zerodivision error
# B == C 인 경우도 있나보다.
# 손익분기점이 존재하지 않으면 -1을 출력한다. 꼼꼼히 읽을 것
if B >= C:
    print(-1)
else:
# profit = -A + (C-B)*count
    count = int(A/(C-B))+1

    print(count)



# 시간초과
# 제한시간 0.35초
# A, B, C = map(int, input().split())

# result = 0

# while True:
#     if A + result * B < result * C:
#         break
#     else:
#         result += 1

# print(result)
