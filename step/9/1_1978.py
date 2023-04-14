# 백준 9단계 기본 수학 2
# 1978번 소수 찾기

import sys
from tabnanny import check

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

T = int(input())
list_input = list(map(int, input().split()))

# print(list_input)

# 소수면 1 아니면 0을 반환한다.
def check_prime_number(n):
    if n == 1:
        return 0
    for i in range(2, n-1):
        if n%i == 0:
            return 0
    
    return 1
count = 0
for number in list_input:
    if check_prime_number(number) == 1:
        count += 1

print(count)

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

