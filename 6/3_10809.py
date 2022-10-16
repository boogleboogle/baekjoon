# 백준 6단계 문자열
# 10809번 알파벳 찾기

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

input_word = input()

list_result = [-1 for i in range(26)]

# print(list_result)

# ord(i)-97로 input world의 문자들이 알파벳의 몇 번째 숫자인지 구한다.
for i in input_word:
    # input_word.find(i)로 처음 나온 알파벳의 위치를 입력해준다.
    list_result[ord(i)-97] = input_word.find(i)

for i in list_result:
    print(i, end=" ")