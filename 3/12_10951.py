# 백준 3단계 반복문
# 10951번 A+B - 4

import sys

from wcwidth import list_versions

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
import sys

# 런타임 에러를 try로 극복하는게 맞는 일일까?
try:
    while True:
        A, B = map(int, input().split())
        print(A + B)
except:
    pass