# 백준 17단계 동적 계획법 1
# 24416번 알고리즘 수업 - 피보나치 수 1

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
N = int(input())


# 코드1
count_1 = 0
def fib(n):
    count_1 += 1
    if n == 1 or n == 2:
        return 1  
    else:
        return (fib(n - 1) + fib(n - 2))


# 코드2
count_2 = 0
f = [0] * 100
def fibonacci(n):
    count += 2
    if n == 1 or n == 2:
        return 1
    if f[n] != 0:
        return f[n]
    f[n] = fibonacci(n-1) + fibonacci(n-2)

    # f[1] <- f[2] <- 1;
    # for i <- 3 to n
    #     f[i] <- f[i - 1] + f[i - 2];  
    # return f[n];


fib(N)
fibonacci(N)
print(count_1, count_2)