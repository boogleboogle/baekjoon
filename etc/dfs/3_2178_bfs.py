# 백준 DFS
# 2178번 미로 탐색

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
N, M = map(int, input().split())

list_maze = []
for i in range(N):
    list_maze.append(input().rstrip())

print(list_maze)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
