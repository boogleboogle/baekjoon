# 백준 13단계 집합과 맵
# 1620번 나는야 포켓몬 마스터 이다솜

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
# # N개의 포켓몬도감
# N, M = map(int, input().split())

# list_poke = [input().rstrip() for _ in range(N)]

# # print(list_poke)

# for i in range(M):
#     my_input = input().rstrip()
#     try:
#         my_input = int(my_input)
#         print(list_poke[int(my_input)-1])
#     except:
#         print(list_poke.index(my_input)+1)
        
# # 시간초과

n, m = map(int, input().split())

dict = {}

for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])