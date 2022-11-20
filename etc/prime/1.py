import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

N = int(input())

count = 0
for i in range(N):
    
    temp = int(input())


    temp_2 = temp**(0.5)

    if temp_2 == int(temp_2):
        count += 1
print(count)