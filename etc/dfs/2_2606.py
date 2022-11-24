# 백준 DFS
# 6630번 로또

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
# # 주어진 컴퓨터의 수 N
# N = int(input())

# # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
# M = int(input())

# list_cpu = [list(map(int, input().split())) for _ in range(M)]
# # print(map(int, input().split()))

# print(list_cpu)

# list_visit = [0 for _ in range(N+1)]
# list_visit[1] = 1
# print(list_visit)

# def dfs():
#     pass

n=int(input()) # 컴퓨터 개수
v=int(input()) # 연결선 개수
graph = [[] for i in range(n+1)] # 그래프 초기화
visited=[0]*(n+1) # 방문한 컴퓨터인지 표시
for i in range(v): # 그래프 생성
    a,b=map(int,input().split())
    graph[a]+=[b] # a에 b 연결
    graph[b]+=[a] # b에 a 연결 -> 양방향
def dfs(v):
    visited[v]=1
    for nx in graph[v]:
        if visited[nx]==0:
            dfs(nx)
dfs(1)
print(sum(visited)-1)


