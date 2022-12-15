# 1. 비밀지도

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(bin(arr1[i] | arr2[i])[2:])
    max_len = 0
    for i in answer:
        if len(i) > max_len:
            max_len = len(i)

    for i in range(len(answer)):
        temp_len = max_len - len(answer[i])
        if temp_len > 0:
            answer[i] = "0"*temp_len + answer[i]
    
    answer_2 = []
    for i in range(len(answer)):
        temp_str = ""
        for j in range(max_len):
            if answer[i][j] == "1":
                temp_str += "#"
            else:
                temp_str += " "
        answer_2.append(temp_str)    

    return answer_2

print(solution(5, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))