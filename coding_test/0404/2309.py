list_height = []
for i in range(9):
    list_height.append(int(input()))

# print(list_height)

total = 100
my_break = 1
for i in range(9):
    for j in range(9):
        if sum(list_height) - list_height[i] - list_height[j] == total and i != j:
            fake_1 = list_height[i]
            fake_2 = list_height[j]

            my_break = 0
        if my_break == 0:
            break
    if my_break == 0:
        break

# print(fake_1, fake_2)

list_height.remove(fake_1)
list_height.remove(fake_2)

# print(list_height)

list_height.sort()

for i in list_height:
    print(i)