# 백준 13단계 집합과 맵
# 10815번 숫자 카드

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
N = int(input())
list_N = list(map(int, input().split()))
M = int(input())
list_M = list(map(int, input().split()))

list_N.sort()

# 이진탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in range(M):
    if binary_search(list_N, list_M[i], 0, N - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')

#######################################################
# list_result = []

# for i in list_M:
#     if i in list_N:
#         list_result.append(1)
#     else:
#         list_result.append(0)

# print(*list_result)
# # 시간초과
#######################################################