test_case = int(input())
# test case의 갯수를 입력 받는다.
 
for test_number in range(test_case):
# test case의 크기만큼 반복한다.
    result = 1
    # 조건에 맞는지 판단하고 출력될 result 변수를 만든다.
    list_standard = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 대조군인 변수 list_standard를 만든다.
    sudoku = []
    for i in range(9):
        input_list = list(map(int, input().split()))
        sudoku.append(input_list)
    # 입력받은 값을 2차원 리스트로 저장한다
    # pprint.pprint(sudoku)
 
    # 3가지 종류의 검증을 거쳐야 한다.
    # 1. 가로축이 조건에 맞는지 확인한다.
 
    for i in sudoku:
        if list_standard != sorted(i):
        # 요소들의 갯수와 종류만 비교하면 되기 때문에 sorted를 사용한다.
            result = 0
 
    # 2. 세로축이 조건에 맞는지 확인한다.
 
    for i in range(9):
        list_length = []
        for j in range(9):
            list_length.append(sudoku[j][i])
        # print(list_length)
 
        if list_standard != sorted(list_length):
            # print(list_length)
            result = 0
 
    # 3*3 사각형이 조건에 맞는지 확인한다.
 
    for i in range(3):
        # print(f'i = {i}')
        for j in range(3):
            # print(f'j = {j}')
            # 우선 3*3인 square를 반복할 2중 반복문을 만든다.
            list_square = []
            for k in range(3):
                # print(f'k = {k}')
                for l in range(3):
                    # print(f'l = {l}')
                    list_square.append(sudoku[k + i * 3][l + j * 3])
                # print(list_square)
            if list_standard != sorted(list_square):
                result = 0
            # k와 l을 이용하여 사각형 모양의 square을 만들어 비교한다.
         
 
    print(f'#{test_number+1} {result}')