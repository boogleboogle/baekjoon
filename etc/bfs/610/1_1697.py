# 백준 강의 알고리즘 기초 2/2 610-BFS
# 1697번 숨바꼭질 

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

# N, K = map(int, input().split())

# list_visit = [[N, K, 0]]

# def next_step(start, goal, depth):

#     next_step_1 = start + 1
#     next_step_2 = start - 1
#     next_step_3 = start * 2
#     depth += 1
#     if next_step_1 not in list_visit:
#         list_visit.append([next_step_1, goal, depth])
#     if next_step_2 not in list_visit:
#         list_visit.append([next_step_2, goal, depth])
#     if next_step_3 not in list_visit:
#         list_visit.append([next_step_3, goal, depth])

# for i in list_visit:
#     start = i[0]
#     goal = i[1]
#     depth = i[2]
#     if start == goal:
#         print(depth)
#         break
#     else:
#         next_step(start, goal, depth)

# list_visit.append([next_step_1, goal, depth]) 메모리 초과    
# if next_step_1 not in list_visit: 시간초과
import sys
from collections import deque

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return array[v]
        for next_v in (v-1, v+1, 2*v):
            if 0 <= next_v < MAX and not array[next_v]:
                array[next_v] = array[v] + 1
                q.append(next_v)


MAX = 100001
n, k = map(int, sys.stdin.readline().split())
array = [0] * MAX
print(bfs(n))
