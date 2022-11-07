import sys
from tabnanny import check

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

N, M = map(int, input().split())
# print(N, M)
list_N = []

for i in range(N):
    list_N.append(input().rstrip())

list_result = []

for i in range(M):
    temp = input().rstrip()
    if temp in list_N:
        list_result.append(temp)

list_result.sort()

if len(list_result) == 0:
    print(-1)
else:
    for i in list_result:
        print(i)

# 오답입니다. (통과하지 못한 테스트케이스가 있습니다.)
# 왜 때문?
