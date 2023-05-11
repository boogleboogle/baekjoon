T = int(input())
 
for test_number in range(T):
    # '0011'
    str_input = input()
 
    count = 0
    if str_input[0] == '1':
        count += 1
     
    for i in range(len(str_input)-1):
        if str_input[i] != str_input[i+1]:
            count += 1
     
    print("#{} {}".format(test_number+1, count))