# 백준 7단계 기본 수학 1
# 2839번 설탕 배달

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.


N = int(input())

# 이 문제는 15가 최소 공약수이기 때문에 이를 이용한다.

count = 0
while True:
    # print(count)
    if N % 15 == 0:
        count += int(N/15) * 3
        N = 0
        break
    elif N % 5 == 0:
        count += int(N/5)
        N = 0
        break
    elif N % 3 == 0:
        count += int(N/3)
        N = 0
        break
    else:
        N -= 3
        count += 1
    
    if N < 3:
        count = -1
        break
print(count)

# 틀렸습니다.
# 3 > 1
# 4 > -1
# 5 > 1
# 6 > 2
# 7 > -1
# 8 > 2
# 9 > 3
# 10 > 2
# 11 > 3
# 12 > 4
# 13 > 3
# 14 > 4
# 15 > 3