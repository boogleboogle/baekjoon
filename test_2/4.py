# K-Digital Training 코딩테스트 모의고사_2회차
# 4번 

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

import sys
import pprint

# 지도의 크기n, 폭탄의 개수 m, 터질 폭탄의 개수 k
n, m, k = map(int, sys.stdin.readline().split())
list_input = [[-1 for i in range(n+2)]]
for i in range(n):
    list_input.append([-1]+list(map(int, sys.stdin.readline().split()))+[-1])
list_input.append([-1 for i in range(n+2)])
pprint.pprint(list_input)

# print(list_input[1][4])
global count
count = 0
def boom(y, x):
    # 폭탄의 위치와 크기를 변수로 담는다.
    size = list_input[y][x]

    # 십자가 모양으로 폭발한다.
    dir_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    # 폭발시킨다.
    list_input[y][x] = 0
    global count
    count += 1

    # 폭발이 연쇄된다.
    for dir in range(4):
        for i in range(1, 1+size):
            now_y = y + dir_list[dir][0]*i
            now_x = x + dir_list[dir][1]*i
            if list_input[now_y][now_x] == -1:
                break
            elif list_input[now_y][now_x] == 0:
                pass
            else:
                boom(now_y,now_x)
        

for i in range(k):
    temp_y, temp_x = map(int, sys.stdin.readline().split())
    boom(temp_y, temp_x)
# print(m)
# print(count)
print(m-count)

# pprint.pprint(list_input)