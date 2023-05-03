test_case = int(input())
# test case의 갯수를 입력 받는다.
 
for test_number in range(test_case):
# test case의 크기만큼 반복한다.
    N = int(input())
    # 숫자의 갯수를 변수 N에 저장한다
    input_list = list(map(int, input().split()))
    # 입력받은 값을 리스트로 만든다.
    input_list.sort()
    # sort를 이용하여 정렬한다.
 
    print(f'#{test_number+1}', end=' ')
    for i in input_list:
        print(i, end=' ')
    print('\n', end='')