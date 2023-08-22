def solution(cipher, code):
    answer = ''
    for i in range(len(cipher)//code):
        answer += cipher[code*i + code-1]
    return answer