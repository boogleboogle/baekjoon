# 백준 3단계 반복문
# 1110번 더하기 사이클

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
import sys
# rstrip()을 넣어서 런타임 해결
N = sys.stdin.readline().rstrip()

if int(N) < 10:
    N = "0" + N

def cycle(N):

    sum_N = int(N[0]) + int(N[1])
    new_N = N[-1] +str(sum_N)[-1]
    return new_N

# print(N)

cycle_len = 1
# N은 input 된 수
# M은 현재 새로운 수
M = cycle(N)
while True:
    # print(M)
    if M == N:
        break
    M = cycle(M)
    cycle_len += 1

   

print(cycle_len)
# 런타임 에러