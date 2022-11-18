# 백준 강의 알고리즘 기초 2/2 611-BFS
# 16948번 데스 나이트

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

N=int(input())

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
