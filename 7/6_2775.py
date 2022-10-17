# 백준 7단계 기본 수학 1
# 2775번 부녀회장이 될테야

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

T = int(input())
for t in range(T):
    # k층, n호
    k = int(input())
    n = int(input())

    # 1층은 직접 만든다.
    list_apt = []
    list_apt.append([i for i in range(1, n + 1)])
    # [[0, 1, 2, 3]]
    # print(list_apt)

    # 0층부터 존재하므로 k+1까지 진행한다.
    for floor in range(1, k+1):
        list_floor = []
        for i in range(n):
            list_floor.append(sum(list_apt[floor-1][0:i+1]))
        
        list_apt.append(list_floor)
    
    print(list_apt[-1][-1])


##########################################################
    # # 보기 쉽게 X, Y로 바꾼다.
    # Y = k
    # X = n

    # list_apt = []
    # for y in range(0, Y):
    #     list_floor = []
    #     for x in range(1, 1 + X):
    #         print(x)
    #         if y == 0:
    #             list_floor.append(x)
    #         elif x == 1:
    #             list_floor.append(list_apt[y-1][x])
    #         else:
    #             list_floor.append(list_apt[y-1][x] + list_floor[-1])
    #     list_apt.append(list_floor) 
    #     print(list_apt)
    # print("11111111111111111111")








