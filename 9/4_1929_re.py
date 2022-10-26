# 백준 9단계 기본 수학 2
# 1929번 소수 구하기

import sys
from tabnanny import check

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.


M, N = map(int, input().split())
# 이중 반복문을 이용하여 깔끔하게 검사 완료.
for i in range(M,N+1):
    if i==1:#1은 소수가 아니므로 제외
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0: #약수가 존재하므로 소수가 아님
            break   #더이상 검사할 필요가 없으므로 멈춤
    else:
        print(i)
