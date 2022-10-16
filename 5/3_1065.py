# 백준 5단계 함수
# 1065번 한수

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

N = int(input())

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 
# 37, 38, 39, 40, 41, 42,, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 111, 123, 135, 147, 159, 210, 222, 234, 246, 
# 258, 321, 333, 345, 357, 369, 420, 432, 444, 456, 468, 531, 543, 555, 567, 579, 630, 642, 654, 666, 678, 741, 753, 765, 777, 789, 840, 852,
# 864, 876, 888, 951, 963, 975, 987, 999, 1000]
list_hs = []

def Add_hs(number):
    str_number = str(number)
    if len(str_number) == 1 or len(str_number) == 2:
        list_hs.append(number)
    elif len(str_number) == 3 and int(str_number[0]) - int(str_number[1]) == int(str_number[1]) - int(str_number[2]):
        list_hs.append(number)
        # 1000일 때는 당연히 아닌데, 왜 맞다고 했을까?
    # elif len(str_number) == 4:
    #     list_hs.append(number)
    else:
        pass

for i in range(1, 1001):
    Add_hs(i)

# print(list_hs)
ans = 0
for i in list_hs:
    if i <= N:
        ans += 1
print(ans)

# 런타임에러(name error)

# N = int(input()) 으로 바꾸고 name error 없어짐.
# elif len(str_number) == 4:
#     list_hs.append(number) 없에고 틀렸습니다. 해결