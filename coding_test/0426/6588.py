import sys

dp = [1] * (1000000 + 1)
dp[0] = 0
dp[1] = 0

for i in range(2, 1001):  #dp에 소수를 넣는 과정 (에라토스테네스의 체)
    if dp[i]:
        for j in range(i * i, 1000001, i):
            dp[j] = 0

def goldba(n):
    for i in range(2, n):
        if dp[i] and dp[n - i]:
            print(f'{n} = {i} + {n - i}')
            return 0 
    return 1    # 골드바흐 가설이 틀린걸 증명 해버림

while (1):
    try:
        n = int(sys.stdin.readline())
        if n == 0: 
            break
        if goldba(n): 
            print("Goldbach's conjecture is wrong.")
    except EOFError:
        break
