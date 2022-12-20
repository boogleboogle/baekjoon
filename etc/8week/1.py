# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
# n = 5

# 수열의 i번이 1부터 셀 경우
# 1 2 3 4     5 6
# 1 2 3 4+3=7 1 6+1=7


# 수열의 i번이 0부터 셀 경우
# 0 1 2 3 4    5 6     7    8      9     10
# 1 2 3 1 4+1  3 6+3   4+1  8+5    6+3   10+6+3
#  
# 짝수일 경우, i + list_seq[i-4] > 계속 짝수
# 홀수일 경우 list_seq[i-3]

list_seq = [1, 2, 3]

result = 0

if n%4 == 0:
	# print("n%4")
	m = int(n/4)
	result = 1
	for i in range(1, m+1):
		result += 4*i

elif (n+1)%4 == 0:
	# print("(n+1)%4")
	m = int((n+1)/4)
	# print(m)
	result = 1
	for i in range(1, m+1):
		result += 4*i
	result -= n+1

elif (n+2)%4 == 0:
	# print("(n+2)%4")
	m = int(n/4)
	result = 3
	for i in range(1, m+1):
		result += 4*i+2

else:
	# print("(n+3)%4")
	m = int(n/4)
	result = 3
	for i in range(1, m+1):
		result += 4*i+2
	result -= n+1
		
print(result)
	