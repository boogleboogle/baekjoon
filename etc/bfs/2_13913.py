# 백준 강의 알고리즘 기초 2/2 610-BFS
# 13913번 숨바꼭질 4

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


from collections import deque

def path(x):
    arr = []
    temp = x
    for _ in range(dist[x]+1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            path(x)
            return x
        for i in (x+1, x-1, 2*x):
            if 0<=i<=100000 and dist[i]==0:
                q.append(i)
                dist[i] = dist[x] + 1
                move[i] = x

N, K = map(int, input().split())
dist = [0]*100001
move = [0]*100001
bfs()
