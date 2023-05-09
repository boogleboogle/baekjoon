T = int(input())
 
for test_number in range(T):
    # 37 1 1
    N, A, B = map(int, input().split())
 
    # R과 C는 1~N-1의 값을 가질 수 있다.
    result = N**4
    for R in range(1, N//2 + 1):
        for C in range(1, N//R + 1):
            if R * C <= N and result > A * abs(R-C) + B * (N - R * C):
                result = A * abs(R-C) + B * (N - R * C)
 
    print("#{} {}".format(test_number+1, result))