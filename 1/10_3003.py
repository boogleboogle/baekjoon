# 백준 1단계 입출력과 사칙연산
# 3003번 킹, 퀸, 룩, 비숍, 나이트, 폰

# 입력과 출력에 관한 문제

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 리스트 요소간의 연산
correct_list = [1, 1, 2, 2, 2, 8]
piece_list = list(map(int, input().split()))

# zip을 이용한다.
answer_list = [correct_i - piece_i for correct_i, piece_i in zip(correct_list, piece_list)]

print(*answer_list)

