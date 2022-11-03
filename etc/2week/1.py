import sys
from tabnanny import check

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

# 구름이가 듣는 수업의 개수 T
T = int(input())
# 각 과목 별 전체 학생 수, 구름이의 등수, 과목별 A+의 성적 순 비율, 과목의 수행평가 개수, A+과목의 수행 평가의 과락 점수의 기준, 구름이가 받은 수행 평가의 점수 

result = 1
for t in range(T):
    list_input = list(map(int, input().split()))

    # 각 과목 별 전체 학생 수
    l = list_input[0]

    # 구름이의 등수
    s = list_input[1]

    # 과목별 A+의 성적 순 비율
    n = list_input[2]

    # 과목의 수행평가 개수
    k = list_input[3]

    # A+과목의 수행 평가의 과락 점수의 기준
    m = list_input[4]

    # 구름이가 받은 수행 평가의 점수 
    for i in range(1, k+1):
        globals()[f"v{i}"] = list_input[4+i]
        if globals()[f"v{i}"] < m:
            result = 0

        

    if s/l > n/100:
        result = 0

print(result)