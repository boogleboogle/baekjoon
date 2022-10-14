# 백준 3단계 반복문
# 1110번 더하기 사이클
# 정명찬님 코드

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

import sys
N = sys.stdin.readline().rstrip()

answer = N
cnt = 0
while True:
    N = N[-1] + str(int(N[0])+int(N[-1]))[-1]
    cnt += 1
    if N == answer:
        break

print(cnt)