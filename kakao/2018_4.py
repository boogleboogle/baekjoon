# 4. n진수 게임

# 이런 게임을 해?


def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return convert_notation(q, base) + T[r] if q else T[r]

def solution(n, t, m, p):
    answer = ''
    answer_2 = ''
    for i in range(10000):
        answer += str(convert_notation(i, n))
    for i in range(p, p*t*m, m):
        answer_2 += answer[i]
    return answer_2




print(solution(16,16,2,1))