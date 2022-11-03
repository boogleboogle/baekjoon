from itertools import count
import sys
from tabnanny import check

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

# 진행한 게임의 수 T
t = int(input())

list_input = list(map(int, input().split()))
# 구르미와 친구의 승리 회수
list_win = [0, 0]

for i in list_input:
    temp = i%4
    if temp == 1 or temp == 3:
        list_win[0] += 1
    else:
        list_win[1] += 1

if list_win[0] == list_win[1]:
    print("tie")
else:
    print(max(list_win))

