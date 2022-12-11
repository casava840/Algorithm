def solution(n):
    answer_list = [0,1]
    for i in range(2,n+1):
        answer_list.append((answer_list[i-2] + answer_list[i-1]) % 1234567)
    return answer_list[-1]