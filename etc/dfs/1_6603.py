# 백준 DFS
# 6603번 로또

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

# 출력이 될 리스트를 생성한다.
dp = [0 for _ in range(13)]

def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(dp[i], end=' ')
        print()
        return
    
    # 재귀로 들어가기 때문에 i를 증가시켜 start로 넣는다.
    for i in range(start, len(arr)):
        dp[depth] = arr[i]
        dfs(i + 1, depth + 1)

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    del arr[0]
    # start = 0, depth = 0
    dfs(0, 0)
    print()