def solution(record):
    answer = []
    dic = {}
    for rec in record:
        temp = rec.split()
        if len(temp) == 3:
            status, uid, character = temp[0], temp[1], temp[2]
        else:
            status, uid, = temp[0], temp[1]
        if status == 'Enter':
            dic[uid] = character
            answer.append((uid, '님이 ' + '들어왔습니다.'))
        elif status == 'Leave':
            answer.append((uid, '님이 ' + '나갔습니다.'))
        else:
            dic[uid] = character
    for i in range(len(answer)):
        x, y = answer[i]
        answer[i] = dic[x] + y
        
    return answer