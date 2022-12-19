# 1. 오픈채팅방

def solution(record):
    for i in range(len(record)):
        record[i] = record[i].split(" ")
    
    db = {}    
    for i in record:
        if len(i) == 3:
            db[i[1]] = i[2]
    # print(db)
    # print(db.get('uid1234'))
    answer = []
    for i in record:
        if i[0] == "Enter":
            answer.append(str(db.get(i[1]))+ "님이 들어왔습니다.")
        elif i[0] == "Leave":
            answer.append(str(db.get(i[1]))+ "님이 나갔습니다.")
                
    return answer



print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))