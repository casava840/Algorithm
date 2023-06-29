def solution(names):
    answer = []
    length = (len(names)-1) // 5 + 1
    for n in range(length):
        answer.append(names[5*n])
    return answer