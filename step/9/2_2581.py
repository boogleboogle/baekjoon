# 백준 9단계 기본 수학 2
# 2581번 소수

import sys
from tabnanny import check

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

M = int(input())
N = int(input())


# 소수면 1 아니면 0을 반환한다.
def check_prime_number(n):
    if n == 1:
        return 0
    for i in range(2, n-1):
        if n%i == 0:
            return 0
    
    return 1


list_prime_number = []

for i in range(M, N+1):
    if check_prime_number(i) == 1:
        list_prime_number.append(i)

# print(list_prime_number)

if len(list_prime_number) == 0:
    print(-1)
else:
    print(sum(list_prime_number))
    print(list_prime_number[0])

# import math
# import time

# start = time.time()
# math.factorial(100000)

# list_temp = []
# for i in range(2, 10000):
#     if check_prime_number(i) == 1:
#         list_temp.append(i)
        
# print(list_temp)
# end = time.time()

# print(f"{end - start:.5f} sec")

