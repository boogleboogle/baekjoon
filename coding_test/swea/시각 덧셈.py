test_case = int(input())
# test case의 갯수를 입력 받는다.
 
for test_number in range(test_case):
# test case의 크기만큼 반복한다.
    hour_1, minute_1, hour_2, minute_2 = map(int, input().split())
    # 입력받은 시각과 분을 변수에 저장한다.
    minute = minute_1 + minute_2
    hour = 0
    if minute > 60:
        minute -= 60
        hour += 1
    # 분을 더해주고, 60분을 초과하면 시간으로 올림한다.
 
    hour += hour_1 + hour_2
    if hour > 12:
        hour -= 12
    # 시간을 더해주고, 12시간을 초과하면 12시간을 빼준다.
 
    print(f'#{test_number+1} {hour} {minute}')