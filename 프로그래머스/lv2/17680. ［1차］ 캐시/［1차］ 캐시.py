def solution(cacheSize, cities):
    cities = list(map(lambda x: x.lower(), cities))
    answer = 0
    que = []
    for city in cities:
        if city in que:
            answer+=1
            que.remove(city)
            que.append(city)
        else:
            answer +=5
            que.append(city)
            if len(que) > cacheSize:
                que.pop(0)
            
    return answer