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


arr = list(map(int, '8 1 2 3 5 8 13 21 34'.split()))

del arr[0]
# start = 0, depth = 0
dfs(0, 0)
