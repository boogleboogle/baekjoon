# 백준 6단계 문자열
# 1316번 그룹 단어 체커

import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

# 여기부터 제출해야 한다.
T = int(input())

ans = 0

def group_word(word):
    list_temp = []
    str_temp = word[0]
    for i in range(len(word)):
        # 처음 보는 알파벳은 list_temp에 추가한다.
        if word[i] not in list_temp:
            list_temp.append(word[i])
            str_temp = word[i]
        # 연속된 알파벳은 넘어간다
        elif word[i] in list_temp and str_temp == word[i]:
            pass
        # 연속되지도 않고, 다시 나타난 알파벳은 그룹단어가 아니게 된다.
        else:
            break
        # 만약 끝까지 문제 없었다면 그룹 단어이다.
        if i == len(word)-1:
            return 1
    return 0


for t in range(T):
    input_word = input()
    ans += group_word(input_word)

print(ans)