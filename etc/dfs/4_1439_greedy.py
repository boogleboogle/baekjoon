# 백준 DFS
# 1439번 뒤집기

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
input_text = input()

input_text = input_text + input_text[0]

count = 0

temp = input_text[0]
for i in range(1, len(input_text)):
    if input_text[i] != input_text[i-1]:
        count += 1


# print(input_text)
print(int(count/2))