# 백준 4단계 1차원 배열
# 1546번 평균

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
import sys

N = int(sys.stdin.readline())
list_input = list(map(int, input().split()))
max_input = max(list_input)

# print(max_input)
modify_score = []
for i in range(N):
    # if list_input[i] == max_input:
    #     modify_score.append(max_input)
    # else:
        modify_score.append((list_input[i]/max_input)*100)

# print(modify_score)
# 소수점 둘 째 자리까지 출력
print(round(sum(modify_score)/N, 2))