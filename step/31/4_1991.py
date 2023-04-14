# 백준 31단계 트리
# 1967번 트리의 지름

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

import pprint
# 여기부터 제출해야 한다.

# 노드의 개수
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())


graph = [[] for _ in range(n + 1)]


def dfs(x, wei):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei + b)


# 부모 노드, 자식 노드, 가중치
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])


pprint.pprint(graph)


distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)
# print(distance)

start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(distance)
print(max(distance))

# RecursionError
# 재귀 깊이 때문에 발생