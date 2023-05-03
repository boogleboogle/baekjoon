import pprint
 
test_case = int(input())
# test case의 갯수를 입력 받는다.
 
for test_number in range(test_case):
# test case의 크기만큼 반복한다.
     
    N, M = map(int, input().split())
    input_list_A = list(map(int, input().split()))
    input_list_B = list(map(int, input().split()))
    # 입력받은 값들을 변수에 저장한다.
 
    list_sum = []
    # 비교해야할 마주보는 숫자들을 곱한 뒤 더한 값을 저장할 list를 만든다.
    if M > N:
        for i in range(M-N+1):
            sum = 0
            for j in range(N):
                sum += input_list_A[j] * input_list_B[j+i]
                # sum에 마주보는 숫자들을 곱한 뒤 더한 값을 저장한다.
            list_sum.append(sum)
 
        print(f'#{test_number+1} {max(list_sum)}')
    else:
        for i in range(N-M+1):
            sum = 0
            for j in range(M):
                sum += input_list_A[j+i] * input_list_B[j]
 
            list_sum.append(sum)
 
        print(f'#{test_number+1} {max(list_sum)}')