# 백준 3단계 반복문
# 10871번 X보다 작은 수

import sys

from wcwidth import list_versions

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
# [참고1](https://www.acmicpc.net/board/view/22716)
# [참고2](https://www.acmicpc.net/blog/view/55)
import sys
N, X = map(int, input().split())
list_input = list(map(int, input().split()))
list_result = []

for i in list_input:
    if i < X:
        list_result.append(i)
print(*list_result)