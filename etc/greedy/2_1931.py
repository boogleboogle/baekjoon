# 백준 강의 알고리즘 중급1/3 710-그리디 알고리즘
# 1931번 회의실 배정

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

N = int(input())

list_meeting = []
for _ in range(N):
    list_meeting.append(list(map(int, input().split())))


# 끝나는 시간이 빠른 순으로 정렬하고, 시작하는 시간이 빠른 순으로 정렬한다.
list_meeting.sort(key=lambda x: (x[1], x[0]))

count = 0
now = 0
for meeting in list_meeting:
    if meeting[0] >= now:
        now = meeting[1]
        count += 1




# print(list_meeting)
print(count)