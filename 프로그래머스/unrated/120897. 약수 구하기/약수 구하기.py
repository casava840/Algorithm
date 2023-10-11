def solution(n):
    i = 1
    answer = []
    while i <= n/2:
        if n % i == 0:
            answer.append(i)
        i += 1
    answer.append(n)
    return answer