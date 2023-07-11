def solution(files):
    temp = []
    answer = []
    for file in files:
        temp_file = []
        num = False
        tail = False
        for i in range(len(file)):
            if file[i].isdigit() and not num and not tail:
                temp_file.append(file[0:i])
                num = True
                if len(file)-1 == i:
                    temp_file.append(file[i])
                    break
            if num and not file[i].isdigit() and not tail:
                temp_file.append(file[len(temp_file[0]):i])
                temp_file.append(file[i:])
                break
            if len(file) - 1 == i and file[i].isdigit() and num and not tail:
                temp_file.append(file[len(temp_file[0]):])
        temp.append(temp_file)
    temp.sort(key = lambda x: int(x[1]))
    temp.sort(key = lambda x: x[0].lower())
    for t in temp:
        s = ''
        for i in range(len(t)):
            s += t[i]
        answer.append(s)
    return answer