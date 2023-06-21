def solution(picture, k):
    answer = []
    
    for i in range(len(picture)):
        temp = picture[i]
        s = ""
        for j in range(len(temp)):
            for _ in range(k):
                s += temp[j]
        for _ in range(k):
            answer.append(s)
    return answer