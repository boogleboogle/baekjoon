# 백준 코딩 테스트 준비 - N과 M
# 15649번 N과 M (1)

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

N, M = map(int, input().split())

print(N, M)

s = []
 
def dfs():
    if len(s)==M:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,N+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
 
dfs()
 