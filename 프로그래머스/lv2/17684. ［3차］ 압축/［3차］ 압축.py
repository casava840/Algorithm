def solution(msg):
    answer = []
    dic = {}
    i = 65
    k = 0
    while len(dic)<26:
        dic[chr(i)] = i-64
        i += 1
    while True:
        j = 2
        while msg[k:k+j] in dic:
            if k+j < len(msg):
                j += 1
            else:
                j += 1
                break
        answer.append(dic[msg[k:k+j-1]])
        dic[msg[k:k+j]] = len(dic) + 1
        k = k+j-1
        if k > len(msg)-1:
            break

    return answer