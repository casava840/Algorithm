def solution(n, words):
    count = 0
    for i in range(1, len(words)):
        if words[i][0]!=words[i-1][-1]:
            count = i+1
            break
        if words[i] in words[0:i]:
            count = i+1
            break
    if count == 0:
        return [0,0]
    else:
        person_num = count%n
        cycle = (count-1)//n+1
        if person_num == 0:
            person_num=n
        return [person_num,cycle]