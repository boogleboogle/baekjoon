# 백준 11단계 재귀
# 11729번 하노이 탑 이동 순서

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# # 여기부터 제출해야 한다.
import math
import time

start = time.time()
math.factorial(100000)

T = int(input())

# def recursion(s, l, r):
#     if l >= r: return 1
#     elif s[l] != s[r]: return 0
#     else: return recursion(s, l+1, r-1)

# def isPalindrome(s):
#     return recursion(s, 0, len(s)-1)

for i in range(T):
    S = input().strip()
    S_reverse = S[::-1]
    # print(S, S_reverse)
    if S == S_reverse:
        count = int(len(S)/2) +1
        print(1, count)
    else:
        count = 0
        for i in range(len(S)):
            if S[i] == S_reverse[i]:
                count += 1
            else:
                break
        count += 1
        print(0, count)



    # print(isPalindrome(S))

# print('ABBA:', isPalindrome('ABBA'))
# print('ABC:', isPalindrome('ABC'))

end = time.time()

print(f"{end - start:.5f} sec")