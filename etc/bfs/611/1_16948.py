# 백준 강의 알고리즘 기초 2/2 611-BFS
# 16948번 데스 나이트

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

from collections import deque
from pprint import pprint
N = int(input())
r1, c1, r2, c2 = map(int, input().split())


dx = [-2, -2, 0, 1, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

# 체스판의 행과 열은 0번부터 시작한다
list_visit = list(list(-1 for i in range(N)) for i in range(N))

list_visit[r1][c1] = 0
# pprint(list_visit)

list_q = [[r1, c1]]


while list_q:
    now = list_q.pop(0)  # 현재위치
    x, y = now[0], now[1]
    
    if x == r2 and y == c2:
        print(list_visit[x][y])
        break
        
    for i in range(6):
        tx = dx[i] + x
        ty = dy[i] + y

        if 0 <= tx < N and 0 <= ty < N  and list_visit[tx][ty] == -1:
            list_q.append([tx,ty])
            list_visit[tx][ty] = list_visit[x][y] + 1

pprint(list_visit)
