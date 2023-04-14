# 백준 9단계 기본 수학 2
# 4948번 베르트랑 공준 

import sys
from tabnanny import check

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
# # 시간초과
# while True:

#     n = int(input())
#     if n == 0:
#         break
#     count = 0
#     # 이중 반복문을 이용하여 깔끔하게 검사 완료.
#     for i in range(n+1,2*n+1):
#         if i==1:#1은 소수가 아니므로 제외
#             continue
#         for j in range(2,int(i**0.5)+1):
#             if i%j==0: #약수가 존재하므로 소수가 아님
#                 break   #더이상 검사할 필요가 없으므로 멈춤
#         else:
#             count += 1

#     print(count)

list_prime_number = []

for i in range(1,2*123456+1):
    if i==1:#1은 소수가 아니므로 제외
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0: #약수가 존재하므로 소수가 아님
            break   #더이상 검사할 필요가 없으므로 멈춤
    else:
        list_prime_number.append(i)

# print(list_prime_number)
while True:
    n = int(input())
    if n == 0:
        break

    count = 0
    # break_point = 0
    for prime_number in list_prime_number:
        if prime_number > n:
            if prime_number <= 2*n:
                count += 1
            else:
                # break_point = 1
                break
            
    print(count)