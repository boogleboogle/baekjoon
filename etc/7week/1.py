# 1번
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def my_function(x):
  if x == 1:
    return 1
  count = 0 
  while True:
    if x == 1:
			# count += 1
      return count
    if x%2 == 0:
      x = x/2
      count += 1
    elif x%2 == 1:
      x += 1
      count += 1

list_2 = [0]
str_2 = "0"
for i in range(1, 10000001):
	str_2 += ", "
	str_2 += str(my_function(i))
f = open("1.txt", 'w')
f.write(str_2)
f.close()