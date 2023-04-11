# 1. 비밀지도

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
    
print(solution(5, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))