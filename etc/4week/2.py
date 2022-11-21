import sys
from tabnanny import check

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
import pprint 

N, M = map(int, input().split())

list_worm = []
for i in range(M):
    list_worm.append(list(input().rstrip()))


# pprint.pprint(list_worm)

# pprint.pprint(list_worm[0])

count = 0
for i in range(M-1,-1,-1):
    temp = 0
    for j in range(N-1,-1,-1):
        if list_worm[i][j] == '1':
            temp += 1
            # print(i,j,count)
        elif temp == 0 and list_worm[i][j] == '0':
            pass
        else:
            break
    count += temp

print(count)

