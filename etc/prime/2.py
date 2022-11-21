import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

N, M = map(int, input().split())

list_result = []

for number in range(N, M+1):
    number_str = str(number)
    temp = 1
    for i in number_str:
        temp = temp * int(i)
    list_result.append(temp)


print(sum(list_result))