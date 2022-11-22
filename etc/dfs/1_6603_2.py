# 백준 DFS
# 6603번 로또

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break

    nums.pop(0)
    V = 6
    stack = []

    def dfs():
        if len(stack) == V:
            print(*stack)
            return

        # 시작 정하기
        if len(stack) == 0:
            for i in nums:
                stack.append(i)
                dfs()
                stack.pop()
            return
        
        for i in nums:
            if i > stack[-1]:
                stack.append(i)
                dfs()
                stack.pop()

    dfs()
    print()