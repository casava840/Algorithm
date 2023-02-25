def solution(word):
    answer = 0
    position = "AEIOU"
    for i, v in enumerate(word):
        answer += position.index(v) * ((5 ** (5-i)) - 1) / 4
        
            
    return answer+len(word)