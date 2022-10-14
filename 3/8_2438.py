# 백준 3단계 반복문
# 2438번 별 찍기 - 1

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
# [참고1](https://www.acmicpc.net/board/view/22716)
# [참고2](https://www.acmicpc.net/blog/view/55)
import sys
N = int(sys.stdin.readline())
for i in range(0, N):
    print("*"*(i+1))