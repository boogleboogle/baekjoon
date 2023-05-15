T = int(input())
 
for test_number in range(T):
    N = int(input())
    list_input = []
     
    for i in range(N):
        list_input.append(list(input()))
    num_mid = int(N/2)
    point_mid = [num_mid, num_mid]
 
 
    total = 0
    for i in range(-1*num_mid, num_mid+1):
        for j in range(-1*num_mid, num_mid+1):
            if abs(i) + abs(j) <= num_mid:
                total += int(list_input[num_mid + i][num_mid + j])
 
    print("#{} {}".format(test_number+1, total))