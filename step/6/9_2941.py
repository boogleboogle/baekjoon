# 백준 6단계 문자열
# 2941번 크로아티아 알파벳

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
input_word = input()

list_Croatian = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

count_Croatian = 0

for word in list_Croatian:
    count_Croatian += input_word.count(word)

print(len(input_word)-count_Croatian)