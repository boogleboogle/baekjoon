# N은 정점의 수, M은 간선의 수, V는 시작 정점
# 간선은 양방향이어서 다시!
# 4 5 1
N, M, V = map(int, (input().split()))
list_square = []
for i in range(M):
    list_square.append(list(map(int, input().split())))

# print(N, M, V)
# [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]]
# print(list_square)
number_max = 0
for i in list_square:
    if number_max <= i[0]:
        number_max = i[0]
    if number_max <= i[1]:
        number_max = i[1]
# 4
# print(number_max)
# [[], [], [], [], []]
list_square_2 = [[] for i in range(number_max+1)]
# print(list_square_2)
# i는 index
for i in range(1, number_max+1):
    for j in list_square:
        if i == j[0]:
            list_square_2[i].append(j[1])
        if i == j[1]:
            list_square_2[i].append(j[0])
# [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
# print('입력데이터', list_square_2)
for i in list_square_2:
    i = i.sort(reverse=True)




# 이제부터 깊이우선탐색!
# print('를정렬하면', list_square_2)
list_stack = [V]
list_visited = [0]*(number_max+1)
list_result = []

# 스택이 빌때까지 반복
while list_stack:

    # 현재위치 재설정
    now = list_stack.pop()

    # 결과값 추가
    if list_visited[now] != 1:
        list_result.append(now)

    # 방문기록 표기
    list_visited[now] = 1


    for j in list_square_2[now]:
        if list_visited[j] != 1:
            list_stack.append(j)
# print('깊이우선탐색결과', list_result)

# 재정렬
for i in list_square_2:
    i = i.sort()
# print('재정렬하면', list_square_2)


# 너비우선탐색
list_stack_2 = [V]
list_visited_2 = [0]*(number_max+1)
list_result_2 = []

while list_stack_2:

    # 현재위치 재설정
    now = list_stack_2.pop(0)

    # 결과값 추가
    if list_visited_2[now] != 1:
        list_result_2.append(now)

    # 방문기록 표기
    list_visited_2[now] = 1


    for j in list_square_2[now]:
        if list_visited_2[j] != 1:
            list_stack_2.append(j)

# print('너비우선탐색결과', list_result_2)
print(*list_result)
print(*list_result_2)