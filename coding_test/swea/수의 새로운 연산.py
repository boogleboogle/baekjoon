def number_coordinates(number):
    for i in range(1, 100000000):
        if number > i:
            number -= i
        else:
            number_count = i-1
            break
    z = number_count + 2
    x = number
    y = z - x
 
    # print(number_count, number)
    return [x, y]
 
 
def coordinates_number(x, y):
    z = x + y
    number = 0
    for i in range(z):
        number += i
    number -= (y-1)
    # print(number)
 
    return number
 
 
T = int(input())
 
for test_number in range(T):
    p, q = map(int, input().split())
 
    # 1. 각 p와 q의 좌표를 구한다.
    list_p = number_coordinates(p)
    list_q = number_coordinates(q)
 
    # p와 q의 각 좌표를 더한다.
    list_sum = [list_p[0]+list_q[0], list_p[1]+list_q[1]]
 
    # 좌표의 숫자를 구한다.
    result = coordinates_number(list_sum[0], list_sum[1])
 
    print("#{} {}".format(test_number+1, result))