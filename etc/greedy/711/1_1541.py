# 백준 강의 알고리즘 중급1/3 711-그리디 알고리즘
# 1541번 잃어버린 괄호

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

text_input = input()
result = 0
list_temp = text_input.split('-')

# for i in list_temp:
#     if i.isdigit():
#         result += int(i)
    # else:
    #     temp = i.split('+')
    #     for j in temp:
    #         result -= int(j)
        # print(temp)

print(list_temp)
print(result)

for i in range(len(list_temp)):
    sum_temp = 0
    temp = list_temp[i].split('+')
    for j in temp:
        sum_temp += int(j)
    if i == 0:
        result += sum_temp
    else:
        result -= sum_temp
print(result)
# for i in list_temp:
#     if i.isdigit():
#         list_temp.remove(i)

# print(list_temp)





