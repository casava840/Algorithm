def solution(citations):
    n = len(citations)
    citations.sort()
    for h in range(0,n+1):
        for i in range(0,n):
            if citations[i]>=h and n-i>=h:
                answer= h

    return answer