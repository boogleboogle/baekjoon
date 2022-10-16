# 백준 6단계 문자열
# 1152번 단어의 개수

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
input_word_list = list(input().split())
print(len(input_word_list))
