def solution(q, r, code):
    answer = ''
    i = 0
    while q*i + r < len(code):
        answer += code[q*i + r]
        i += 1
        
    return answer