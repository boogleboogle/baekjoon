# 백준 4단계 1차원 배열
# 4344번 평균은 넘겠지

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
import sys
C = int(sys.stdin.readline())

def get_result():
    list_score = list(map(int, input().split()))

    num_score = list_score[0]
    list_score = list_score[1:]
    avg_score = sum(list_score)/num_score
    num_over_avg = 0
    for i in list_score:
        if i > avg_score:
            num_over_avg += 1
    # 0을 채우는 소수점 자리수를 위하여 f-string을 사용한다.
    print(f"{(num_over_avg/num_score)*100:.3f}%")
    # 런타임에러
    # return 0으로 해결(FileNotFoundError)
    # https://help.acmicpc.net/judge/rte/NZEC ?
    return 0

for i in range(C):
    get_result()