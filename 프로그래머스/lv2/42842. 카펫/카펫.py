def solution(brown, yellow):
    sum=brown + yellow
    answer=[]
    for i in range(3,sum):
        if sum%i == 0:
            answer.append(i)
    print('answer: ',answer)
    for i in range(0, len(answer)):
        for j in range(i, len(answer)):
            if answer[i]*answer[j]==sum and answer[i]+answer[j]-2==brown/2:
                return [answer[j],answer[i]]
                break