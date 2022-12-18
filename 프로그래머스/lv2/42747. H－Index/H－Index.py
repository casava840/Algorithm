def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()
    #1. citations 
    for i in range(n):
        if citations[i] > n-i:
            answer = citations[i-1]
            break
    return answer