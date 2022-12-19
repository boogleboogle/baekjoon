# 3. 후보키

# lru 원리
# https://dailylifeofdeveloper.tistory.com/355

def solution(cacheSize, cities):
    cities = cities.upper()
    answer = 0
    list_cache = []
    for i in cities:
        i = i.upper()
        # 캐쉬에 없을 경우
        if i not in list_cache:
            # 자리가 있을 때
            if len(list_cache) < cacheSize:
                list_cache.append(i)
            # 자리가 없을 때
            else:
                list_cache.append(i)
                del list_cache[0]
            answer += 5
        # 캐쉬에 있을 경우
        else:
            index_i = list_cache.index(i)
            del list_cache[index_i]
            list_cache.append(i)
            answer += 1


    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))