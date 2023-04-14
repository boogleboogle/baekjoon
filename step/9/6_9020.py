# 백준 9단계 기본 수학 2
# 9020번 골드바흐의 추측

import sys
from tabnanny import check

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 시간초과
# 여기부터 제출해야 한다.
list_prime_number = []

for i in range(2,10000+1):
    if i==1:#1은 소수가 아니므로 제외
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0: #약수가 존재하므로 소수가 아님
            break   #더이상 검사할 필요가 없으므로 멈춤
    else:
        list_prime_number.append(i)
    
# print(list_prime_number)

T = int(input())
for t in range(T):
    n = int(input())
    m = int(n/2)
    breakpoint = 0
    for prime_number in list_prime_number:
        if prime_number >= m:
            m_close_prime_number = prime_number
            m_close_index = list_prime_number.index(prime_number)
            break
    # print(m_close_index, m_close_prime_number)

    for index in range(m_close_index, 0-1, -1):
        for index_2 in range(m_close_index, m_close_index+100):
            # print(index, index_2)
            if list_prime_number[index] + list_prime_number[index_2] == n:
                print(list_prime_number[index], list_prime_number[index_2])
                breakpoint = 1
                break
            elif list_prime_number[index] + list_prime_number[index_2] > n:
                # print("elif")
                break
        if breakpoint == 1:
            break


    

    


    

    # list_gold = []
    # for prime_number in list_prime_number:
    #     if prime_number > m:
    #         break
    #     for prime_number_2 in list_prime_number:
    #         if prime_number + prime_number_2 == n:
    #             list_gold.append([prime_number, prime_number_2])

    # print(list_gold[-1][0], list_gold[-1][1])
