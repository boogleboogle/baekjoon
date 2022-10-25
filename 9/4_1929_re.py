# 백준 9단계 기본 수학 2
# 1929번 소수 구하기

import sys
from tabnanny import check

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.


M, N = map(int, input().split())

list_prime_number = []
list_temp = [i for i in range(2, 1000000+1)]

for i in range(2, 1000000+1):
    for j in list_temp:
        if i == j:
            list_temp.append(i)
            for k in list_temp:
                if k%i == 0:
                    list_temp.pop(k)

print(list_prime_number)



