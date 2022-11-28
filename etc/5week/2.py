# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 집의 개수 n, 이사 횟수 k
n, k = map(int, input().split())
# print(n, k)
list_v = list(map(int, input().split()))

# print(list_v)

list_count = [10000000]*(n+1)
# print(list_count)
for i in list_v:
	if list_count[i] == 10000000:
		list_count[i]=1
	else:
		list_count[i] += 1

# print(list_count)
my_min = min(list_count)
# print(my_min)

result = 0 
for i in range(len(list_count)):
	if list_count[i] == my_min:
		result += i
	
print(result)
# 오답입니다. (통과하지 못한 테스트케이스가 있습니다.)
