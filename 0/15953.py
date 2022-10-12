import sys

# 표준 입력을 파일로 설정하기 -> input.txt를 읽어들여옴
sys.stdin = open("input.txt", "r") 

# 1 ≤ T ≤ 1,000
N = int(input())

# ex) [[8, 4], [13, 19], [8, 10], [18, 18], [8, 25], [13, 16]]
list_input = []
for i in range(0, N):
    list_input.append(list(map(int, input().split())))

list_1 = [500, 300, 200, 50, 30, 10]
list_1_p = [1, 3, 6, 10, 15, 21]
# [512, 256, 128, 64, 32]
list_2 = list(2**(9-i) for i in range(0, 5))
# [1, 3, 7, 15, 31]
list_2_p = list(2**(i+1)-1 for i in range(0, 5))

# print(list_2)
# print(list_2_p )

for i in list_input:
    # 각 대회 상금
    A = 0
    B = 0
    # 예상 등수
    a = i[0]
    b = i[1]
    # print(a, b)
    for j in range(len(list_1_p)):
        # 0의 예외 처리를 해주지 않아 틀렸음.!
        if a == 0:
            break
        elif list_1_p[j] >= a:
            A = list_1[j]
            # print(A)
            break
    for k in range(len(list_2_p)):
        if b == 0:
            break
        elif list_2_p[k] >= b:
            B = list_2[k]
            # print(B)
            break


    print((A + B)*10000)
