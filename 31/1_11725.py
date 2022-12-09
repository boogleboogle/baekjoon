# 백준 17단계 동적 계획법 1
# 24416번 알고리즘 수업 - 피보나치 수 1

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
N=int(input())
visited=[False]*(N+1)
answer=[0]*(N+1)
E=[[] for _ in range(N+1)]
for i in range(N-1):
    S,D=map(int,input().split())
    E[S].append(D)
    E[D].append(S)


def dfs(E,v,visited):
    visited[v]=True
    for i in E[v]:
        if not visited[i]:
            answer[i]=v
            dfs(E, i, visited)
            

dfs(E,1,visited)


for i in range(2,N+1):
        print(answer[i])