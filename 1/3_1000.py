# 백준 1단계 입출력과 사칙연산
# 1000번 A+B

# 입력과 출력에 관한 문제
# 평소 input()을 사용했지만 https://www.acmicpc.net/blog/view/56 를 참고하여 realine을 사용하기로 한다.

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

A, B = map(int, input().split())

print(A+B)

# https://uhhyunjoo.tistory.com/67 도 잘 정리되어 있어 참고가 되었다.