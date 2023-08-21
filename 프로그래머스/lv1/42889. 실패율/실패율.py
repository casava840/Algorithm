
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
def solution(N, stages):
    answer = []
    rate = []
    fail = [0]*N
    total_user = len(stages)
    while stages:
        temp = stages.pop(-1)
        if temp < N+1:
            fail[temp-1] += 1
    for i in range(N):
        if fail[i] != 0:
            rate.append([fail[i]/total_user,i+1])
            total_user -= fail[i]
        else:
            rate.append([0,i+1])

    rate.sort(key = lambda x: x[0] ,reverse=True)
    for i in range(len(rate)):
        answer.append(rate[i][1])
    return answer