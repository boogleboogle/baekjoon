# 백준 5단계 함수
# 4673번 셀프 넘버

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

def d(n):
    str_n = str(n)
    for i in str_n:
        n += int(i)
    return n

list_10000 = list(i for i in range(1, 10001))

for i in range(1, 10001):
    temp = d(i)
    if temp <= 10000:
        try:
            list_10000.remove(temp)
        except:
            pass

for self_number in list_10000:
    print(self_number)