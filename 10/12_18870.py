# 백준 10단계 정렬
# 18870번 좌표 압축

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# # 여기부터 제출해야 한다.
# N = int(input())
# list_input = list(map(int, input().split()))

# # 중복제거
# set_input = set(list_input)
# list_input_s = list(set_input)

# # 정렬
# list_input_sorted = sorted(list_input_s)

# # 비어있는 리스트
# list_x = list('x' for i in range(N))


# # print(list_input)
# # print(list_input_sorted)
# # print(list_x)

# for i in range(N):
#     list_x[i] = list_input_sorted.index(list_input[i])

# print(*list_x)

# 시간초과

# https://gudwns1243.tistory.com/52 참고
# list.index(i) 형태의 시간 복잡도 = O(N)
# index[i] 형태의 시간 복잡도 = O(1)

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
dic = {arr2[i] : i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end = ' ')