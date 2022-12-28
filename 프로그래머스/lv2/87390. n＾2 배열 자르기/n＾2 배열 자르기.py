def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        extra = i % n
        share = i // n
        if extra <= share:
            answer.append(share+1)
        else:
            answer.append(extra+1)
    return answer