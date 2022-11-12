import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.

N = int(input())

list_input = list(map(int, input().split()))


def MergeSort(list):
    if len(list) <= 1: 
        return list

    mid = len(list) // 2 
    left = MergeSort(list[:mid])
    right = MergeSort(list[mid:])
    return Merge(left,right) 

def Merge(left,right): 
    merged_list = [] 
    left_P, right_P = 0,0 

    
    #case 1: left/right가 아직 남아있을 때
    while len(left) > left_P and len(right) > right_P:
        if left[left_P] > right[right_P]:
            merged_list.append(right[right_P]) 
            right_P += 1
        else : 
            merged_list.append(left[left_P])
            left_P += 1
    
    #case 2: left만 남았을 때
    while len(left) > left_P :
        merged_list.append(left[left_P])
        left_P += 1
        
    #case 3: right만 남았을 때
    while len(right) > right_P :
        merged_list.append(right[right_P]) 
        right_P += 1
        
    # print(merged_list)
    return merged_list

# print(list_input)
print(*MergeSort(list_input))