# 백준 6단계 문자열
# 5622번 다이얼

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
input_word = input()

def get_time(w):
    if w == "A" or w == "B" or w == "C":
        return 3
    elif w == "D" or w == "E" or w == "F":
        return 4
    elif w == "G" or w == "H" or w == "I":
        return 5
    elif w == "J" or w == "K" or w == "L":
        return 6
    elif w == "M" or w == "N" or w == "O":
        return 7
    elif w == "P" or w == "Q" or w == "R" or w == "S":
        return 8
    elif w == "T" or w == "U" or w == "V":
        return 9
    else:
        return 10

result_time = 0
for i in input_word:
    result_time += get_time(i)

print(result_time)
###################################################
# input_word = input()

# def get_time(w):
#     result = int((ord(w) - 62)/3) +2
#     return result

# result_time = 0
# for i in input_word:
#     result_time += get_time(i)

# print(result_time)
# # 틀렸습니다.
# # 4개씩 배열된 숫자가 있음.