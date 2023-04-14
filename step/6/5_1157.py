# 백준 6단계 문자열
# 1157번 단어 공부

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

# 대문자로 처리한다.
input_word = input().upper()

# 중복을 제거한다.
list_word = list(set(input_word))

# print(input_word)
# print(list_word)

# 각 알파벳과 알파벳의 개수를 dictionary형태로 만든다.
dict_count = {}
for i in list_word:
    dict_count[i] = input_word.count(i)

list_values = list(dict_count.values())
# print(list_values)
max_value = max(dict_count.values())
# print(max_value)

if list_values.count(max_value) > 1:
    print("?")
else:
    # 키와 벨류의 순서쌍을 바꾼다
    reverse_dict= dict(map(reversed,dict_count.items()))
    print(reverse_dict.get(max_value))

