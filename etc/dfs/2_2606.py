# 백준 DFS
# 6630번 로또

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
# 주어진 컴퓨터의 수 N
N = int(input())

# 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
M = int(input())

list_cpu = [list(map(int, input().split())) for _ in range(M)]
# print(map(int, input().split()))

print(list_cpu)

list_visit = [0 for _ in range(N+1)]
list_visit[1] = 1
print(list_visit)

def dfs():
    pass


