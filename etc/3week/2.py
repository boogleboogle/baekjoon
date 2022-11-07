from itertools import count
import sys
from tabnanny import check

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

# 상인, 귀족, 시민의 수
n, m, k = map(int, input().split())

list_n = list(map(int, input().split()))
list_m = list(map(int, input().split()))
list_k = list(map(int, input().split()))

# print(list_n)

list_vote = [(i, 0) for i in range(1, 4235)]
dict_vote = dict(list_vote)


for i in list_n:
    dict_vote[i] += 2

for i in list_m:
    dict_vote[i] += 3

for i in list_k:
    dict_vote[i] += 1

# print(dict_vote)

print(max(dict_vote, key=dict_vote.get))

# 오답입니다. (통과하지 못한 테스트케이스가 있습니다.)