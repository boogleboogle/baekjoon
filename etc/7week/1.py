# 1번
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n = int(input())
# print(n)

list_knee = []

for i in range(n):
	list_knee.append(list(map(int, input().split())))
	
# # print(list_knee)

# list_loc = []
# for i in range(n):
# 	for j in range(n):
# 		if list_knee[i][j] == 1:
# 			list_loc.append([i,j])
			
# print(list_loc)

# my_top = max(list_loc, key=lambda x:x[1])[1]
# my_bottom = min(list_loc, key=lambda x:x[1])[1]
# my_right = max(list_loc, key=lambda x:x[0])[0]
# my_left = min(list_loc, key=lambda x:x[0])[0]

# print(my_top, my_bottom, my_right, my_left)
# print((my_top - my_bottom + 1)*(my_right - my_left + 1))
my_top = -1
my_bottom = -1
my_right = -1
my_left = -1

# top
break_point = 0
for y in range(n):
	for x in range(n):
		if list_knee[y][x] == 1:
			my_top = y
			break_point = 1
			break
	if break_point == 1:
		break
		
# bottom
break_point = 0
for y in range(n-1, -1, -1):
	for x in range(n):
		if list_knee[y][x] == 1:
			my_bottom = y
			break_point = 1
			break
	if break_point == 1:
		break



# left
break_point = 0
for x in range(n):
	for y in range(n):
		if list_knee[y][x] == 1:
			my_left = x
			break_point = 1
			break
	if break_point == 1:
		break

		
# right
break_point = 0
for x in range(n-1, -1, -1):
	for y in range(n):
		if list_knee[y][x] == 1:
			my_right = x
			break_point = 1
			break
	if break_point == 1:
		break
		
		
		
			
# print(my_top, my_bottom, my_right, my_left)
print((my_bottom - my_top+ 1)*(my_right - my_left + 1))

