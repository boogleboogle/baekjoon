# 백준 10단계 정렬
# 25305번 커트라인

import sys
from tabnanny import check

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
# 응시자 수 N, 상을 받는 사람의 수 K
N, K = map(int, input().split())
list_input = list(map(int, input().split()))


def my_sort(list_t):
    list_t = list_t
    N = len(list_t)

    # nlogn
    for i in range(N):
        for j in range(N):
            if list_t[i] > list_t[j]:
                list_t[i], list_t[j] = list_t[j], list_t[i]

    return list_t
# print(my_sort(list_input))
print(my_sort(list_input)[K-1])