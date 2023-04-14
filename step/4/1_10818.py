# 백준 4단계 1차원 배열
# 10818번 최소, 최대

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
import sys
N = sys.stdin.readline()
list_input = list(map(int, input().split()))

print(f"{min(list_input)} {max(list_input)}")
