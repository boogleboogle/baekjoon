# 백준 2단계 조건문
# 2884번 알람 시계

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
# [참고](https://docs.python.org/3.8/library/datetime.html#strftime-and-strptime-format-codes)
import datetime
H, M = map(int, input().split())

# datetime.time은 timedelta연산이 안되기 때문에, datetime.datetime을 사용했다.
alarm = datetime.datetime(2022, 10, 12, H, M)
result = alarm + datetime.timedelta(minutes=-45)

# %H, %M은 앞자리 숫자를 0으로 채우는 2자리 숫자로 표현되기 때문에 int로 바꿔준다.
result_H = int(result.strftime("%H"))
result_M = int(result.strftime("%M"))
print(result_H, result_M)

