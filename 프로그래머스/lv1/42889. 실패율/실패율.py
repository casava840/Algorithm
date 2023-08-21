def solution(N, stages):
    answer = {}
    fail = [0]*N
    total_user = len(stages)
    while stages:
        temp = stages.pop(-1)
        if temp < N+1:
            fail[temp-1] += 1
    for i in range(N):
        if fail[i] != 0:
            answer[i+1] = fail[i] / total_user
            total_user -= fail[i]
        else:
            answer[i+1] = 0
            
    return sorted(answer, key = lambda x: answer[x] ,reverse=True)