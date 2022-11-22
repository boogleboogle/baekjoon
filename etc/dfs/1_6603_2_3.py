# 백준 DFS
# 6603번 로또

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

while True:
    nums = list(map(int, input().split()))
    if nums == [0]:
        break

    nums.pop(0)
    # 숫자 6개를 고르는 문제이다.
    V = 6
    stack = []

    def dfs():
        # stack이 6개를 모두 채웠으면 출력하고 끝낸다.
        if len(stack) == V:
            print(*stack)
            return

        # 시작을 정한다.
        if len(stack) == 0:
            for i in nums:
                stack.append(i)
                dfs()
                stack.pop()           
        else:
            for i in nums:
                # stack에 더 들어갈 수 있는 숫자가 남아있다면 넣는다.
                if i > stack[-1]:
                    stack.append(i)
                    dfs()
                    stack.pop()

    dfs()
    print()