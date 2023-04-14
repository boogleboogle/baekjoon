# 백준 3단계 반복문
# 10952번 A+B - 5

import sys

from wcwidth import list_versions

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
import sys

while True:
    N, X = map(int, input().split())
    if N == X == 0:
        break
    else:
        print(N + X)
