# 백준 6단계 문자열
# 5622번 다이얼

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

import sys
def han(Num):
    arr = []
    cnt = 0
    tmp =0
    if(Num>=100):
        cnt = 99
        for k in range(100,Num+1):
            tmp = k
            while(tmp != 0): #각 자리수 arr에
                arr.append(tmp%10)
                tmp = tmp//10
            if((arr[0]-arr[1])==(arr[1]-arr[2])):
                cnt += 1
                print(k)
            arr = []
        return cnt
    else: ## 99이하의 수는 한수로 분류
        return Num
N = int(sys.stdin.readline().rstrip())
print(han(N))