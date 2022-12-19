# K-Digital Training 코딩테스트 모의고사_2회차
# 3번 

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

import sys

n = int(sys.stdin.readline())
list_input = []
for i in range(n):
    list_input.append(int(sys.stdin.readline()))


# print(n, list_input)

# 처음에 1개
# 2 3

from functools import lru_cache

# @lru_cache(maxsize=None)
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)


# n = 3
# print('Fibonacci({}): {}'.format(n, fib(n)))

list_fib = [1, 1, 2]
for i in range(27):
    list_fib.append(list_fib[i+1] + list_fib[i+2])

list_sum_fib = [0]
for i in range(27):
    list_sum_fib.append(list_sum_fib[i] + list_fib[i])

list_sum_fib = list_sum_fib[1:]
# print(list_fib)
# print(list_sum_fib)

for i in list_input:
    for j in range(27):
        if i <= list_sum_fib[j]:
            print(j)
            break