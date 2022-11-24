import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
# https://www.acmicpc.net/problem/6603

N = int(input())
list_wine = list(map(int, input().split()))


print(sum(list_wine)-min(list_wine)*N)