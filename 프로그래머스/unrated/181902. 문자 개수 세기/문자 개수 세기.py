def solution(my_string):
    larger = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    smaller = 'abcdefghijklmnopqrstuvwxyz'
    answer = [0] * 52
    for i in range(len(my_string)):
        temp = my_string[i]
        if temp.isupper():
            index = larger.find(temp)
        else:
            index = smaller.find(temp) + 26
        answer[index] += 1
    return answer