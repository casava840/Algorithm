def solution(n):
    answer = 0
    a = 1
    while a < (n ** 0.5):
        b = n//a
        if a*b == n:
            answer += 1
        a += 1
    if (n ** 0.5)%1 == 0:
        return answer*2 + 1
    else:
        return answer*2