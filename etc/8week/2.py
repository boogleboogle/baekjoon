# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n, k = map(int, input().split())

import datetime

# d1 = datetime.timedelta(hours = 23, minutes = 10)
# d2 = datetime.timedelta(hours = 23, minutes = 10)

# d3 = d2-d1

# print(d3/datetime.timedelta(hours=1))

# 공부한 시간
dict_time = {}
# list_name = []
# 입력된 시간
list_time = []
for i in range(n):
	input_time, input_name = input().split(' ')
	input_hour, input_minute = map(int, input_time.split(':'))
	# print(input_hour, input_minute, input_name)
	list_time.append([input_name, datetime.timedelta(hours = input_hour, minutes = input_minute)])
	dict_time[input_name] = [0, 0]

for i in list_time:
	# input_time, input_name = input().split(' ')
	# input_hour, input_minute = map(int, input_time.split(':'))
	# print(input_hour, input_minute, input_name)
	# 처음 공부하는 사람의 경우를 먼저 처리한다. 	
	# not in을 안쓸 수 없을까?	
	# if input_name not in dict_time.keys():
	# if input_name not in list_name:
	# 	list_name.append(input_name)
		
		# print(1)
		# 이름:[누적공부시간, 입장시간]	형식으로 딕셔너리에 추가해준다.
		# dict_time[input_name] = [0, datetime.timedelta(hours = input_hour, minutes = input_minute)]
	#	입장 할 때 입장시간을 기록한다.
	# elif dict_time[input_name][1] == 0:
	input_name = i[0]
	if dict_time[input_name][1] == 0:
		dict_time[input_name][1] = i[1]
	# 퇴장 할 때 공부한 시간을 기록한다.
	else:
		# 입장시간
		d1 = dict_time[input_name][1]
		# 퇴장시간
		d2 = i[1]
		# 공부시간
		d3 = d2 - d1
		study_time = int(d3/datetime.timedelta(minutes=1))
		# 자정을 넘어서 공부 했을 경우에 24시간을 더해 고쳐준다.		
		if study_time < 0:
			study_time += 24*60
		# 기존에 공부한 시간에서 새로 공부한 시간을 추가한다.
		dict_time[input_name][0] += study_time
		# 입장시간을 0으로 초기화 한다.
		dict_time[input_name][1] = 0

			

	
# print(dict_time)

# 공부시간이 일정 시간 이상 되는 학생들의 수를 센다.
count = 0
for i in dict_time.values():
	if i[0] >= k*60:
		count += 1
		# print(i)
print(count)

# 통과하지 못한 테스트케이스가 있습니다.
# 시간초과?